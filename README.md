# FreeD
## College project. Development currently suspended.
Travis CI checks removed due to elimination of free plan tier for OSS. A new equivalent CI/CD tool will be required.

Debt Growth Outlook Visualization and Repayment Decision Assitant

![GitHub](https://img.shields.io/github/license/Luigi-PastorePica/FreeD) 
![Travis (.com)](https://img.shields.io/travis/com/Luigi-PastorePica/FreeD) 
![Codecov](https://img.shields.io/codecov/c/github/Luigi-PastorePica/FreeD) 
![Codacy grade](https://img.shields.io/codacy/grade/0ea833b9dcd040cb95b179e1df147e66)
![Read the Docs](https://img.shields.io/readthedocs/freed)

[Repo's Page](https://github.com/Luigi-PastorePica/FreeD)

[Documentation](https://freed.readthedocs.io/en/latest)

## FreeD in a nutshell (What is it?)

A tool that leverages multiple visualizations to show at a glance the outlook for multiple debts. By having a visual representation based on the input data, the user can easily realize which debts would cost more in the long term, helping in the decision of which one to repay more agressively first.


## Motivation

When managing debt, you usually want to save money. As a result, it is recommended to calculate which debt is costing you more money in the long term regarding accrued interest and pay that one more agressively. 

Every couple of months, after doing some payments, I find myself re-calculating which debt is growing faster in order to adjust where to allocate money above the minimum payments. This is a relatively simple process when dealing with a few accounts, but it becomes tedious to do repeatedly and periodically for several accounts. 

## Objective

The intention of this project is to create a simple personal finance tool for saving money when repaying debt. This application would allow to keep track of credits and loans, their interest rates, how much is still owed, mothly minimums, etc. Such data will be used to calculate and recommend which debt(s) to pay above the minimum at that particular time and, if the same amount is paid each month, at which point that debt is no longer the one accruing the most interest (in absolute values, not percentages).

The idea is that the user can clearly see which debts are the fastest growing, helping them evaluate which are more beneficial to pay more aggressively first (and up to what amount) in order to save money in the long term and extablish a roadmap to free themselves from debt.


## Some Features that Might be Included
- Easily modify values for remaining principal, interest rate, minimum payment, budget available (these are variable, so this feature would be really useful).
- Present the user with a table of debts/loans that can be ordered based on different criteria.
- Draw a plot, graph, or some other visualization that shows the projected change of the different balances (principal and interest) based on current data.

# Running a Dev Container
In the root directory, run
```bash
docker build -f .devcontainer/Dockerfile -t freed-dev .
```

## Developing in the devcontainer

This repository includes a `.devcontainer` configuration so you can open and edit the project inside a reproducible development container (VS Code or PyCharm). The devcontainer mounts the repository into the container at `/workspaces/FreeD` so edits you make locally are immediately visible inside the container.

Quick steps (VS Code)

1. Install Docker and the VS Code Dev Containers extension.
2. Open this repository folder in VS Code (open the repo root).
3. Command Palette (Cmd+Shift+P) → `Dev Containers: Reopen in Container`.
4. VS Code will build the image and start the `app` service using `.devcontainer/docker-compose.yml`. Your workspace will be mounted at `/workspaces/FreeD` inside the container.
5. (Optional) Connect to the container via terminal. You can forego this step and go directly to the Docker app and enter the container's terminal instead.
```Bash
docker run --rm -it -v "$(pwd)":/workspaces/FreeD -w /workspaces/FreeD freed-dev /bin/bash
```
6. Use the Docker app's integrated terminal and run tests or the app:
```bash
# from inside the container terminal (or in the mounted workspace)
cd /workspaces/FreeD
python -c "from freed.debt_class import Debt; print('import ok')"
pytest
```


Handling dependencies

- The devcontainer `Dockerfile` installs `uv` and the Docker build runs `uv sync` to bake dependencies into the image. The `.devcontainer/devcontainer.json` also runs `uv --no-cache sync` as a `postCreateCommand` so the running container has dependencies installed when the devcontainer starts.
- If you edit `pyproject.toml` to change dependencies, re-run `uv --no-cache sync` inside the container (from `/workspaces/FreeD`) or rebuild the devcontainer image (Command Palette → `Dev Containers: Rebuild and Reopen in Container`).

PyCharm (Docker Compose interpreter)

1. Configure Docker in PyCharm preferences (Preferences → Tools → Docker).
2. Add a Python interpreter → Docker Compose, point it to `.devcontainer/docker-compose.yml`, and select the `app` service.
3. Ensure path mappings map your local project root to `/workspaces/FreeD` in the container.

Notes and troubleshooting

- The image build copies only `pyproject.toml` and `uv.lock` into the image during build to run `uv sync`. The full project is mounted at runtime; this allows live editing without rebuilding the image every change.
- If files appear missing, verify the container mounts the workspace at `/workspaces/FreeD` (check the running container's `ls -la /workspaces/FreeD`).
- If dependency installation fails, check for missing OS-level build deps and add them in the Dockerfile's apt-get section.
