# Literature Matrix

Append new papers to the main table. Keep partial information rather than
waiting for a perfect citation.

## Main Table

| Status | Paper / Filename | Year | Theme Tags | Method Family | Environment / Domain | Key Idea | Relevance to This Repo | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Seed theme | Q-learning foundations | TBD | q-learning, td-learning, value-based | Value learning | General RL | Baseline temporal-difference control and exploration concepts. | Useful for explaining independent learner baselines and reward-learning intuition. | Add canonical paper or textbook source when chosen. |
| Seed theme | Policy gradient foundations | TBD | policy-gradient, actor-critic | Policy optimization | General RL | Directly optimize parameterized stochastic policies. | Background for PPO, MAPPO, COMA, and actor-critic variants. | Add canonical source and variance-reduction notes. |
| Seed theme | DQN-style methods | TBD | dqn, replay-buffer, target-network | Deep value learning | Discrete control | Stabilized neural Q-learning for discrete action spaces. | Candidate independent-DQN baseline for grid actions, with non-stationarity caveats. | Track implementation assumptions if IDQN is added. |
| Seed theme | PPO / MAPPO | TBD | ppo, mappo, centralized-training | Policy optimization / CTDE | Cooperative MARL | PPO updates with centralized training signals and decentralized policies. | Strong candidate baseline because `TaskAllocationEnv.state()` exposes global state. | Identify exact MAPPO reference and implementation notes. |
| Seed theme | VDN / QMIX / QTRAN | TBD | vdn, qmix, qtran, value-decomposition | Cooperative value decomposition | Team-reward MARL | Learn per-agent utilities and combine them into a joint action-value estimate. | Natural fit for cooperative task completion and credit-assignment experiments. | Compare assumptions and data requirements before implementation. |
| Seed theme | COMA | TBD | coma, counterfactual-baseline, credit-assignment | Actor-critic / CTDE | Cooperative MARL | Uses a counterfactual advantage baseline to assign credit to agents. | Useful comparator for credit assignment under shared task reward. | Add note on action-space requirements and critic inputs. |
| Seed theme | MADDPG-style actor-critic | TBD | maddpg, centralized-critic, decentralized-actor | Actor-critic / CTDE | Multi-agent control | Centralized critics train decentralized actors in multi-agent settings. | Helps frame CTDE design even if the current environment uses discrete actions. | Decide whether to study discrete adaptations or keep as conceptual background. |
| Seed theme | Communication in MARL | TBD | communication, coordination, partial-observability | Communication / coordination | Cooperative MARL | Agents learn or use messages to coordinate under partial observability. | Relevant if local observations limit task discovery or assignment quality. | Track whether communication is needed before adding env channels. |
| Seed theme | UAV task allocation | TBD | uav, task-allocation, routing, scheduling | Application domain | UAV / robotics | Multi-agent assignment, routing, servicing, energy, and timing constraints. | Provides domain requirements for scaling beyond the current grid-world sandbox. | Add domain papers as filenames become known. |

## Append Template

| Status | Paper / Filename | Year | Theme Tags | Method Family | Environment / Domain | Key Idea | Relevance to This Repo | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| To read | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Status Labels

- `To read`: paper identified but not reviewed.
- `Skimmed`: title, abstract, and main contribution checked.
- `Noted`: detailed note exists.
- `Implemented`: paper informed code or experiment setup.
- `Background`: useful context but not expected to drive implementation.
- `Seed theme`: repo-known topic placeholder, not a precise citation.

## Tag Suggestions

Use comma-separated tags so rows stay searchable:

`q-learning`, `dqn`, `policy-gradient`, `ppo`, `mappo`,
`value-decomposition`, `vdn`, `qmix`, `qtran`, `coma`, `maddpg`,
`ctde`, `credit-assignment`, `communication`, `partial-observability`,
`uav-task-allocation`, `routing`, `energy`, `reward-shaping`,
`pettingzoo`, `baseline`.
