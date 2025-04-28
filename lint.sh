#!/bin/sh

isort arda setup.py
black arda setup.py
flake8 --max-line-length=88 --ignore=E203 arda setup.py
