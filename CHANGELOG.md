# Changelog

All notable updates to this MARL simulation repository will be tracked here.

## 2026-05-05

- Added Docker support with `Dockerfile`, `docker-compose.yml`, and `.dockerignore`.
- Added a starter PettingZoo `ParallelEnv` for cooperative task allocation.
- Added smoke tests for the environment API and observation/step behavior.
- Updated local activation script to include `PYTHONPATH`.
- Verified the stack locally and inside Docker.

## 2026-04-30

- Created the initial Python 3.12 virtual environment.
- Added `requirements-marl.txt` for the MARL software stack.
- Added `activate_marl.sh` for local development setup.
- Added `.gitignore` to avoid committing virtual environments, caches, experiment outputs, and local research PDFs.
