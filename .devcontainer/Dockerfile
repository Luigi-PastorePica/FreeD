FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

ENV PYTHONUNBUFFERED=1

# Install uv package manager so we can use it instead of pip
RUN python -m pip install --no-cache-dir uv

# Copy project metadata and lockfile where uv will read them
COPY pyproject.toml uv.lock /tmp/uv-tmp/

# Use uv to sync packages (run from the project dir so uv reads pyproject.toml and uv.lock), then cleanup
RUN cd /tmp/uv-tmp && uv --no-cache sync \
    && rm -rf /tmp/uv-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
