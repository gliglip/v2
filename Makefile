.PHONY: clean release test

clean:
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .tox

test:
	py.test

test-codacy:
	py.test --cov-report xml --cov .

release:
	python setup.py sdist bdist_wheel register upload -s
