# Research Questions

Use this file to keep the reading list connected to implementation choices.
Prefer practical questions that can be answered by a paper note, a small
experiment, or a design decision.

## Open Questions

| Question | Why It Matters | Related Themes | Evidence Needed | Status |
| --- | --- | --- | --- | --- |
| What should the first baseline be: independent Q-learning/DQN, IPPO, MAPPO, VDN, or QMIX? | Baseline choice shapes the training loop and evaluation harness. | q-learning, dqn, ppo, mappo, vdn, qmix | Paper notes plus implementation complexity estimate. | Open |
| Does the current global `state()` contain enough information for MAPPO, COMA, or QMIX-style centralized training? | CTDE methods depend on a useful centralized training signal. | ctde, mappo, coma, value-decomposition | Compare required critic or mixer inputs against environment state. | Open |
| How should credit assignment be measured when all agents receive team reward for completed tasks? | Shared rewards can hide whether coordination or individual learning improves. | credit-assignment, coma, value-decomposition | Metrics for task completions, idle movement, duplicate service attempts, and time-to-completion. | Open |
| When does communication become necessary rather than decorative? | Communication channels add complexity and should answer a real partial-observability limitation. | communication, partial-observability, coordination | Experiments varying observation radius, task visibility, and agent count. | Open |
| Which UAV task-allocation constraints should be introduced first after the grid-world baseline? | Domain realism should be added incrementally without breaking learning signal clarity. | uav-task-allocation, routing, energy, scheduling | Domain paper notes and a staged environment roadmap. | Open |
| How should reward shaping balance fast task completion against efficient movement and fair workload distribution? | Reward details can dominate learning behavior. | reward-shaping, task-allocation, credit-assignment | Ablation plan comparing sparse, shaped, and team-only rewards. | Open |
| Which algorithms scale best as agents and tasks increase? | The repo will need stress tests beyond the small sandbox. | mappo, qmix, vdn, communication | Scaling experiments with fixed seeds and comparable budgets. | Open |

## Candidate Experiments

| Experiment | Research Link | Minimal Setup | Metric |
| --- | --- | --- | --- |
| Independent learner baseline | Q-learning / DQN / IPPO | Current `TaskAllocationEnv` with local observations. | Mean completed tasks, episode length, return variance. |
| CTDE policy-gradient baseline | PPO / MAPPO | Use local observations for actors and `state()` for centralized critic. | Sample efficiency and completion rate. |
| Value decomposition baseline | VDN / QMIX / QTRAN | Team reward with per-agent local observations and joint state where required. | Coordination quality and scalability. |
| Credit-assignment comparison | COMA / value decomposition | Track duplicate service attempts and idle steps. | Reduced wasted actions and faster completion. |
| Communication stress test | Communication MARL | Restrict local task visibility or increase grid size. | Benefit of messages over no-message baseline. |
| UAV realism step | UAV task allocation | Add energy budget, service duration, or task deadlines one at a time. | Constraint satisfaction and reward stability. |

## Answered Questions

Move resolved questions here with the date and evidence source.

| Date | Question | Answer | Evidence |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |
