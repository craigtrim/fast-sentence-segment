ifeq ($(OS),Windows_NT)
	os_shell := powershell
	download_en_core_web_sm := .\resources\scripts\download-spacy-model.ps1
else
	os_shell := bash
	download_en_core_web_sm := ./resources/scripts/download-spacy-model.sh
endif

get_model:
	$(os_shell) $(download_en_core_web_sm)

# -----------------------------------------------------------------

install:
	poetry check
	poetry lock
	poetry update
	poetry install
	poetry run pip freeze > requirements.txt

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

all:
	make get_model
	make build
	make linters
	poetry run python -m pip install --upgrade pip
