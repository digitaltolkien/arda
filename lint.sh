#!/bin/sh

isort arda
black arda
flake8 --max-line-length=88 arda

