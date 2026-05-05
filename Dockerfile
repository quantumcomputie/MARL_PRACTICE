FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    MPLCONFIGDIR=/workspace/.mplconfig

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libglib2.0-0 \
        libgl1 \
        libxext6 \
        libsm6 \
        libxrender1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-marl.txt .
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements-marl.txt

COPY . .
RUN mkdir -p /workspace/.mplconfig

CMD ["bash"]
