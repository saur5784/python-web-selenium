# Slack web client ui automation #

### Env Setup
- Download the project zip file and unzip it
- `cd <project_root_directory>`
- Install [Brew](https://docs.brew.sh/Installation)
- Install pipenv using `brew install pipenv`
- Install pytest using `pipenv install pytest --dev`
- Install selenium using `pipenv install selenium --dev
` 
 

### Executing tests

```
- Edit config.json (inside resources) and configure <base_url> <username> <password>
- From <project_root_directory>
pipenv run python -m pytest
```
### Project structure
- root
    - pages
    - tests
        - test_*.py
        - conftest
    - resources
        - drivers
        - config.json
    - utils
    - README
    