.PHONY: help deps docs test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 deps 	install all external dependencies"
	@echo "  docs	create pydocs for all relveant modules"
	@echo "	 test	run all tests with coverage"

docs:
	@echo "... generating docs"
	bash rcli/scripts/make_docs.sh
	ls -l docs

dev:
	pip install coverage
	pip install pylint
	pip install -e .

test:
	coverage run -m unittest discover
	coverage html