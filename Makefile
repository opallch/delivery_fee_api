.PHONY: all venv hooks lint analyse test run run-in-docker
.IGNORE: analyse

include .env
export

PROJECT_NAME = delivery_fee_api
FLASK_PORT=8080
VENV_NAME ?= venv
PYTHON = ${VENV_NAME}/bin/python
SYS_PYTHON = python3.10

all: venv hooks

${VENV_NAME}/bin/activate: requirements.txt dev-requirements.txt
	${SYS_PYTHON} -m venv ${VENV_NAME}
	${PYTHON} -m pip install -r requirements.txt
	${PYTHON} -m pip install -r dev-requirements.txt
venv: ${VENV_NAME}/bin/activate

hooks:
	cp .githooks/* .git/hooks/
	chmod a+x .git/hooks/*

lint: venv
	${PYTHON} -m pylint ${PROJECT_NAME} test -E
	${PYTHON} -m flake8 ${PROJECT_NAME} test \
	    --per-file-ignores "test/*:E501"

test: venv
	${PYTHON} -m pytest test --tb=long -s

run: venv
	${PYTHON} -m flask --app ${PROJECT_NAME} run --port ${FLASK_PORT} --debug

clean:
	rm -rf $(VENV_NAME)

requirements.txt: requirements.in
	${SYS_PYTHON} -m venv requirements
	requirements/bin/pip install -r requirements.in
	requirements/bin/pip freeze > requirements.txt
	rm -rf requirements
