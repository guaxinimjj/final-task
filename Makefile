black:
	python -m black .

lint:
	python -m pylint department_app

test:
	python -m pytest tests

ci:
	make black
	make lint
	make test
	coveralls
