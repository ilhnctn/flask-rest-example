CURRENT_DIRECTORY := $(shell pwd)

help:
	@echo "=========== Welcome to Klarna App makefile Help ==========="
	@echo "=========== Example usages are as below. ==========="
	@echo "make up 		=> To start docker-compose environment (docker-compose up --build)"
	@echo "make tail 	=> Show docker-compose logs"
	@echo "make cli		=> SSH into app (web) shell"
	@echo "make ipython	=> SSH into app (web) ipython shell"

up:
	@docker-compose up --build

down:
	@docker-compose down


start:
	@docker-compose start

stop:
	@docker-compose stop

status:
	@docker-compose ps

restart: stop start

clean: stop
	@docker-compose rm --force
	@find . -name \*.pyc -delete

test:
	@pytest

test_docker:
	@docker-compose run --rm web pytest

cli:
	@docker-compose run --rm web bash

ipython:
	@docker-compose run --rm web ipython

tail:
	@docker-compose logs -f

.PHONY: start stop status restart clean test up down migrate cli tail