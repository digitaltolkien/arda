#!/bin/sh

coverage run -m doctest -v test.rst
coverage html
coverage report -m