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

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build
	make copy_setup

mypy:
	poetry run mypy climate_bot
	poetry run stubgen .\fast_sentence_segment\ -o .

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

pyc:
	poetry run python -c "import compileall; compileall.compile_dir('fast_sentence_segment', optimize=2, force=True, legacy=True)"
	poetry run python -c "import compileall; compileall.compile_dir('fast_sentence_segment', optimize=2, force=True, legacy=False)"

freeze:
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make get_model
	make build
#	20221019; haven't run this yet
#	make mypy
	make linters
	make pyc
	make freeze
