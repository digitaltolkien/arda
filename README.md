# arda

Python library for Tolkien-related data processing

This project is in its early stages and currently just has two things.

Firstly, an initial implementation of `Year` and `YearDelta` classes for
dealing with Ages and the beginnings of a Shire Calendar class `ShireDate`.

See `test.rst` for an example.

Secondly, a syllabification library for breaking Elvish words into
syllables and calculating where the stress should go.

See `pron_test.rst` for an example.


## Development

Install the dev dependencies in `Pipfile`.

Then run `test.sh` to test or `lint.sh` to lint.
