from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="arda",
    version="0.1.0",
    description="Python library for Tolkien-related data processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/digitaltolkien/arda",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    license="MIT",
    packages=["arda"],
)
