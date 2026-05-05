# MARL Practice

Research sandbox for building and testing multi-agent reinforcement learning simulations.

## Project Updates

Track repository changes in [CHANGELOG.md](CHANGELOG.md).

## Research Tracking

Use [docs/research/README.md](docs/research/README.md) to add paper notes,
maintain the literature matrix, and connect readings to implementation
questions.

## Local Environment

```bash
source ./activate_marl.sh
export PYTHONPATH="$PWD/src"
pytest
```

## Docker Environment

```bash
docker compose build
docker compose run --rm marl
```

Run the same container checks used by CI:

```bash
docker compose run --rm test
docker compose run --rm demo
```

## Training Scaffold

The first training target is an IPPO-style PPO baseline for `TaskAllocationEnv`.
The initial config lives at [configs/ippo_task_allocation.yaml](configs/ippo_task_allocation.yaml),
with RLlib environment helpers in `src/marl_practice/training/`.

## First Environment

`TaskAllocationEnv` is a small PettingZoo `ParallelEnv` where multiple agents move on a 2D grid and complete active tasks. It is intentionally simple so it can become the baseline target for IPPO/MAPPO, QMIX, VDN, and custom reward-shaping experiments.
