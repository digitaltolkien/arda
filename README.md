# arda

Python library for Tolkien-related data processing

This project is in its early stages and currently just has two things.

Firstly, an initial implementation of `Year` and `YearDelta` classes for
dealing with Ages and the beginnings of a Shire Calendar class `ShireDate`.

See `test.rst` for an example.

Secondly, a pronunciation library capable of converting Elvish words into IPA
and syllabifying them with a stress marker.

See `pron_test.rst` for an example.


## Development

Install the dev dependencies in `requirements-dev.txt`.

Then run `test.sh` to test or `lint.sh` to lint.
