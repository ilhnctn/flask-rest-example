# Klarna Sample App
This project creates an API to implement a few mathematical algorithms over REST API.

### Development Stack
This app is developed on Python 3.8.3 and Flask 1.1.2.
It also depends on Redis as well.
You can either run the app on docker containers or run from local environments (like pyenv or virtualenv)

## Installation Guide
Before cloning the project; cache/database engine (Redis) service must be ready.
You can either use docker-compose or install locally to manage these dependencies 

After this step, clone the project and navigate into the project root.

### Installation On Local Env

```bash
➜ git clone git@github.com:ilhnctn/klarna.git
➜ cd klarna && python -m venv venv && source venv/bin/activate
➜ python -m pip install -r requirements/development.txt 
```

## Local Settings & Database Credentials
You must copy the dist env file as below and fill your credentials.

```bash
➜ cp envs/dev.env.sample  envs/dev.env
```

### Installation On Docker
```bash
➜ git clone git@github.com:ilhnctn/klarna.git && cd klarna
➜ docker-compose up --build 
```

You can also follow the [Makefile](./Makefile) to see more instructions about server management.

After either of the steps above, the api will be up and running on http://localhost:8080 (or whatever port supplied in docker-compose)
[This link](https://www.getpostman.com/collections/7b17273f0c4d357d00a8) contains an up-to-date Postman collection for all api services.

### Tests
Test suits depend on pytest and coverage (not mandatory).

**Important**: Test dependencies are contained in development.txt requirements file, together with development and debug tools. 
In staging environments, this can be separated as well.

```bash
(venv) ➜  klarna git:(develop) ✗ pytest
(venv) ➜ # or to run specific test
(venv) ➜  klarna git:(develop) ✗ pytest apps/fibonacci/tests/test_service.py -k test_fails_when_unsupported_input_sent
(venv) ➜ # If you want to generate code coverage 
(venv) ➜  klarna git:(develop) ✗ coverage run -m pytest
```

### Notes and Missing Topics
- [ ] Caching: Add Redis layer on list endpoints
- [ ] Add custom Exception handling and improve logging
- [ ] pep8 & flake
- [x] Tests
    - [x] Service Tests
    - [ ] Model Tests
    - [x] View Tests
