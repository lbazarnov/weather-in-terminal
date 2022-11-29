install:
	poetry install

weatherapp:
	poetry run weather_in_terminal

build:
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 weather_in_terminal