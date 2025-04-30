#

setup:
	rm -fr venv
	python3 -m venv venv

install:
	pip install -r requirements.txt

download_data:
	python3 src/data_processing/download_data.py
