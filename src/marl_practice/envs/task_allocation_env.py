from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from gymnasium import spaces
from pettingzoo import ParallelEnv


@dataclass(frozen=True)
class Task:
    position: np.ndarray
    active: bool = True


class TaskAllocationEnv(ParallelEnv):
    """Small cooperative task-allocation environment.

    Agents move on a square grid and receive team reward for serving active
    tasks. Observations are local but the environment exposes `state()` for
    centralized-training algorithms.
    """

    metadata = {"name": "task_allocation_v0", "render_modes": ["ansi"]}

    ACTIONS = {
        0: np.array([0, 0], dtype=np.int32),   # no-op
        1: np.array([0, 1], dtype=np.int32),   # up
        2: np.array([0, -1], dtype=np.int32),  # down
        3: np.array([-1, 0], dtype=np.int32),  # left
        4: np.array([1, 0], dtype=np.int32),   # right
    }
    SERVE = 5

    def __init__(
        self,
        num_agents: int = 3,
        num_tasks: int = 4,
        grid_size: int = 8,
        max_cycles: int = 50,
        render_mode: str | None = None,
    ) -> None:
        if num_agents < 1:
            raise ValueError("num_agents must be at least 1")
        if num_tasks < 1:
            raise ValueError("num_tasks must be at least 1")
        if grid_size < 2:
            raise ValueError("grid_size must be at least 2")

        self.possible_agents = [f"agent_{idx}" for idx in range(num_agents)]
        self.num_tasks = num_tasks
        self.grid_size = grid_size
        self.max_cycles = max_cycles
        self.render_mode = render_mode

        self._action_spaces = {
            agent: spaces.Discrete(len(self.ACTIONS) + 1)
            for agent in self.possible_agents
        }
        self._observation_spaces = {
            agent: spaces.Box(low=0.0, high=1.0, shape=(6,), dtype=np.float32)
            for agent in self.possible_agents
        }

        self.agents: list[str] = []
        self.agent_positions: dict[str, np.ndarray] = {}
        self.tasks: list[Task] = []
        self.steps = 0
        self.np_random = np.random.default_rng()

    def observation_space(self, agent: str) -> spaces.Box:
        return self._observation_spaces[agent]

    def action_space(self, agent: str) -> spaces.Discrete:
        return self._action_spaces[agent]

    def reset(self, seed: int | None = None, options: dict | None = None):
        del options
        self.np_random = np.random.default_rng(seed)
        self.agents = self.possible_agents[:]
        self.steps = 0

        self.agent_positions = {
            agent: self.np_random.integers(0, self.grid_size, size=2, dtype=np.int32)
            for agent in self.agents
        }
        self.tasks = [
            Task(
                position=self.np_random.integers(0, self.grid_size, size=2, dtype=np.int32),
                active=True,
            )
            for _ in range(self.num_tasks)
        ]

        observations = {agent: self._observe(agent) for agent in self.agents}
        infos = {agent: {} for agent in self.agents}
        return observations, infos

    def step(self, actions: dict[str, int]):
        if not self.agents:
            return {}, {}, {}, {}, {}

        self.steps += 1
        rewards = {agent: -0.01 for agent in self.agents}

        for agent, action in actions.items():
            if agent not in self.agents:
                continue
            if action == self.SERVE:
                rewards[agent] += self._serve_task(agent)
                continue
            move = self.ACTIONS.get(int(action), self.ACTIONS[0])
            next_position = self.agent_positions[agent] + move
            self.agent_positions[agent] = np.clip(next_position, 0, self.grid_size - 1)

        all_done = not any(task.active for task in self.tasks)
        truncated = self.steps >= self.max_cycles
        terminations = {agent: all_done for agent in self.agents}
        truncations = {agent: truncated for agent in self.agents}
        observations = {agent: self._observe(agent) for agent in self.agents}
        infos = {agent: {"active_tasks": self.active_task_count} for agent in self.agents}

        if all_done or truncated:
            self.agents = []

        return observations, rewards, terminations, truncations, infos

    def state(self) -> np.ndarray:
        agent_state = np.concatenate(
            [self.agent_positions[agent] / (self.grid_size - 1) for agent in self.possible_agents]
        )
        task_state = np.concatenate(
            [
                np.array(
                    [
                        task.position[0] / (self.grid_size - 1),
                        task.position[1] / (self.grid_size - 1),
                        float(task.active),
                    ],
                    dtype=np.float32,
                )
                for task in self.tasks
            ]
        )
        return np.concatenate([agent_state, task_state]).astype(np.float32)

    def render(self) -> str:
        grid = np.full((self.grid_size, self.grid_size), ".", dtype=object)
        for idx, task in enumerate(self.tasks):
            if task.active:
                x, y = task.position
                grid[self.grid_size - 1 - y, x] = f"T{idx}"
        for idx, agent in enumerate(self.possible_agents):
            if agent in self.agent_positions:
                x, y = self.agent_positions[agent]
                grid[self.grid_size - 1 - y, x] = f"A{idx}"
        return "\n".join(" ".join(cell.rjust(2) for cell in row) for row in grid)

    def close(self) -> None:
        return None

    @property
    def active_task_count(self) -> int:
        return sum(task.active for task in self.tasks)

    def _observe(self, agent: str) -> np.ndarray:
        position = self.agent_positions[agent].astype(np.float32)
        nearest = self._nearest_active_task(position)
        if nearest is None:
            nearest_position = position
            active_flag = 0.0
        else:
            nearest_position = nearest.position.astype(np.float32)
            active_flag = 1.0

        delta = nearest_position - position
        return np.array(
            [
                position[0] / (self.grid_size - 1),
                position[1] / (self.grid_size - 1),
                nearest_position[0] / (self.grid_size - 1),
                nearest_position[1] / (self.grid_size - 1),
                np.linalg.norm(delta, ord=1) / (2 * (self.grid_size - 1)),
                active_flag,
            ],
            dtype=np.float32,
        )

    def _nearest_active_task(self, position: np.ndarray) -> Task | None:
        active_tasks = [task for task in self.tasks if task.active]
        if not active_tasks:
            return None
        return min(active_tasks, key=lambda task: np.linalg.norm(task.position - position, ord=1))

    def _serve_task(self, agent: str) -> float:
        position = self.agent_positions[agent]
        for idx, task in enumerate(self.tasks):
            if task.active and np.array_equal(task.position, position):
                self.tasks[idx] = Task(position=task.position, active=False)
                return 1.0
        return -0.05


if __name__ == "__main__":
    env = TaskAllocationEnv()
    observations, _ = env.reset(seed=7)
    print("Initial observations:", observations)
    print(env.render())
