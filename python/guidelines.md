# Python Guidelines

- Versioning
- Code style
- Documentation
  - Inline
  - External
- Typing
- Testing
- Packaging
- Logging
- Coding



## Code style

You should adhere to PEP8.

Resources:




## Documentation

You MUST document your code inline using docstrings.
You SHOULD use the Google style. It is more readable than the ReStructured Text 
(RST). *Add link to Google style* 

Sphinx.


## Code style

PEP8
Must pass Use flake8:
  McCabe complexity
  pycodestyle (formerly pep8, stylistic)
  pyflakes (logical)
  pydocstyle (formerly pep257)
Optional: MyPy for static type checking
pylint is logical and stylistic
May use black to autoformat

The flake8 configuration can be inside the setup.cfg, tox.ini or .flake8 file
or passed as comand line arguments:
```ini
ignore = E305
exclude = .git,__pychache__
max-line-length = 90
```

## Testing philosophy

Individual test steps with expected outcome is outdated:
As well as the classic "test pyramid":
https://tryexceptpass.org/article/pytest-github-integration/


## Typing

pyright: Microsoft alternative to mypy

## Linting

List of rules for flake8: https://lintlyci.github.io/Flake8Rules/


## Packaging

- src or not? 
  - See [python bytes 22](https://pythonbytes.fm/episodes/show/22/pythonpath-considered-harmful)
  - https://hynek.me/articles/testing-packaging/
  - See [python bytes 15](https://pythonbytes.fm/episodes/show/15/digging-into-python-packaging)
- https://python-packaging.readthedocs.io/en/latest/
- [Simple introduction](https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5#.b9ww4h4xt)
- [Current by attrs' maintainer](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)
- [Extensive overview](http://andrewsforge.com/article/python-new-package-landscape/)
- [PyCon video on packaging](https://www.youtube.com/watch?time_continue=1&v=AQsZsgJ30AE&feature=emb_logo)
- [Brian Skinn: setuptools and pyproject.toml](https://bskinn.github.io/My-How-Why-Pyproject-Src/)
- [Test & Code with Brett Cannon](https://testandcode.com/52)

## Test automation

- [tox on python bytes 44](https://pythonbytes.fm/episodes/show/44/pip-install-malicious-code)
- [tox changedir instead of src](https://pythonbytes.fm/episodes/show/138/will-pyoxidizer-weld-shut-one-of-python-s-major-gaps)

## Laguage core

- Python patterns https://python-patterns.guide/

## Standard library

Asyncio
- [Yeray Diaz on Hackernoon](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e#.ft56qol06)
- [Chris Medina on tryexceptpass](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32#.8qk30tq31)
- [Chrie Medina: new asyncio features in 3.7](https://tryexceptpass.org/article/asyncio-in-37/)

## Third party

CLI
- [fire: convert functions and object to cli](https://github.com/google/python-fire)
