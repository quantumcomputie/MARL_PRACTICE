import numpy as np
from pettingzoo.test import parallel_api_test

from marl_practice.envs.task_allocation_env import TaskAllocationEnv


def test_parallel_api_contract():
    env = TaskAllocationEnv(max_cycles=5)
    parallel_api_test(env, num_cycles=10)


def test_reset_and_step_shapes():
    env = TaskAllocationEnv(num_agents=2, num_tasks=2, grid_size=5, max_cycles=3)
    observations, infos = env.reset(seed=42)

    assert set(observations) == {"agent_0", "agent_1"}
    assert set(infos) == {"agent_0", "agent_1"}
    assert observations["agent_0"].shape == (6,)
    assert observations["agent_0"].dtype == np.float32

    actions = {agent: env.action_space(agent).sample() for agent in env.agents}
    observations, rewards, terminations, truncations, infos = env.step(actions)

    assert set(observations) == {"agent_0", "agent_1"}
    assert set(rewards) == {"agent_0", "agent_1"}
    assert set(terminations) == {"agent_0", "agent_1"}
    assert set(truncations) == {"agent_0", "agent_1"}
    assert set(infos) == {"agent_0", "agent_1"}
    assert env.state().dtype == np.float32
