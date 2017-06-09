.PHONY: clean test test-codacy lint

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete

test:
	cd app; py.test

test-codacy:
	cd app; py.test --cov-report xml --cov .

lint:
	cd app; flake8
	isort --check-only --recursive
