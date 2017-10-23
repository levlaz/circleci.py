.PHONY: help dev docs test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "  docs	create pydocs for all relveant modules"
	@echo "	 test	run all tests with coverage"

dev:
	pip install coverage
	pip install pylint
	pip install -e .

docs:
	@echo "... generating docs"
	bash scripts/make_docs.sh
	ls -l docs

test:
	coverage run -m unittest discover
	coverage html