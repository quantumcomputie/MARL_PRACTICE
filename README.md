# MARL Practice

Research sandbox for building and testing multi-agent reinforcement learning simulations.

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

Inside the container:

```bash
pytest
python -m marl_practice.envs.task_allocation_env
```

## First Environment

`TaskAllocationEnv` is a small PettingZoo `ParallelEnv` where multiple agents move on a 2D grid and complete active tasks. It is intentionally simple so it can become the baseline target for IPPO/MAPPO, QMIX, VDN, and custom reward-shaping experiments.
