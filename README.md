# Bot_mem

- [Getting Started](#getting-started)
- [Project Features](#project-features)
    - [Makefile](#makefile)
    - [Pre Commit](#pre-commit)


## Getting Started
After clone or init git repo you need to call init command.
```
make init
```
After that you need to set environment variables in ```.env``` and ```config.yaml``` files.

The next step is to build the project.
```
make build
```
When the web is fully built you can continue to configure the project.
```
make full-migrate   # makemigrations and migrate
make admin          # createsuperuser
make collectstatic  # collectstatic
```

## Project Features
This project is built on DRF and PostgreSQL.

### Makefile
This project uses **Makefile**. List of make commands:

```
make init
make build
make web-logs
make full-migrate   # makemigrations and migrate
make admin          # createsuperuser
make collectstatic  # collectstatic
```

### Pre-Commit
This project uses [pre-commit](https://pre-commit.com/). List of base linters:
- black
- flake8
- isort
