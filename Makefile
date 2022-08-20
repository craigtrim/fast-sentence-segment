ifeq ($(OS),Windows_NT)
	os_shell := powershell
	download_en_core_web_sm := .\resources\scripts\download-en_core_web_sm.ps1
else
	os_shell := bash
	download_en_core_web_sm := .\resources\scripts\download-en_core_web_sm.sh
endif

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


get_model:
	$(os_shell) $(download_en_core_web_sm)

all:
	make get_model
	make build
	poetry run python -m pip install --upgrade pip
