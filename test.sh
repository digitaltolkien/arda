#!/bin/sh

coverage run -m doctest -v test.rst
coverage run --append -m doctest -v pron_test.rst
coverage html
coverage xml
coverage report -m
