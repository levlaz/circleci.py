#!/bin/bash

##
# Find all python files that are not env, tests, or __init__
# and generate pydocs for them with their full module path
# into the docs/ folder.
##

source env/bin/activate

find . -name "*.py" | \
  grep -v "__init__.py" | \
  grep -v "./env/" | \
  grep -v "./tests/" | \
  grep -v "setup.py" | \
  grep -v "build" | \
  while read line; do
    pydoc $line > docs/$(echo $line | sed 's/\//./g' | sed 's/..//' | sed 's/.py/.txt/')
  done
