#

.PHONY: setup install download clean train runserver migrate

VENV_DIR := venv

PYTHON := $(VENV_DIR)/bin/python3

PIP := $(VENV_DIR)/bin/pip

setup:
	rm -rf $(VENV_DIR)
	python3 -m venv $(VENV_DIR)

install:
	source $(VENV_DIR)/bin/activate
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

download:
	$(PYTHON) src/data_processing/download_data.py

clean:
	$(PYTHON) src/data_processing/clean_data.py

train:
	$(PYTHON) src/model_training/train_classification.py

runserver:
	$(PYTHON) src/manage.py runserver

migrate:
	$(PYTHON) src/manage.py migrate
