# Branch dev-imporve-dev-container
- Fix hanging build issue. Failure to connect to the container at end of build.
  - Is this really an issue? I only seee when explicitly running `docker-compose up`. I haven't tried just running the devcontainer in Docker and trying to connect Pycharm backend.
  - Is PyCharm backend to be defined in the devcontainer.json?

# Consider moving the below items to a GH issue.

# New branch
- Create a script that will generate both .env file samples. This way, I can create setup steps that say "run this script first to set up your .env files".
- Explain that the .env files are gitignored for security reasons.
- Explain that that .env files need manual update depending on developer's local setup.
- Update README.md to reflect new setup steps.
- Tell developers they must download Postgres first if they want to use local Postgres instead of containerize it.
- I may want to add postgres DB setup to the script, if possible.
- Advanced: Add prompts to the script to customize .env files based on developer's needs.