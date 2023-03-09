ifeq ($(OS),Windows_NT)
	os_shell := powershell
	copy_setup := resources/scripts/copy_setup.ps1
	download_en_core_web_sm := .\resources\scripts\download-en_core_web_sm.ps1
else
	os_shell := bash
	copy_setup := resources/scripts/copy_setup.sh
	download_en_core_web_sm := .\resources\scripts\download-en_core_web_sm.sh
endif

copy_setup:
	$(os_shell) $(copy_setup)

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
	make copy_setup

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

all:
	make get_model
	make build
	make linters
	make freeze
	poetry run python -m pip install --upgrade pip
