.PHONY: install lint test run docker-build docker-run

install:
	pip install -r requirements-dev.txt

lint:
	ruff check .

test:
	pytest --cov=app

run:
	python -m app.main

docker-build:
	docker build -t cicd-playground:local .

docker-run:
	docker run --rm -p 8000:8000 cicd-playground:local
