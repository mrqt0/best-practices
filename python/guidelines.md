# Python Guidelines

>
>
>

Let's face it, python packaging is a mess. Share and reuse software across the
company. Aid for anyone. If we use similar practives, we can benefit from each
other. Not everyone should have to figure out.
Libraries for build, test and process automation inside Rohde & Schwarz. 
Mission statement in inneRSource.

Purpose: how do you write quality library and bring it to pypi.rsint.net.
How to use this code, dependency managent etc. is a different topic.

Anyone who wants to write a package may use this docuement as a reference.
Anyone who decides to follow the rules has a chance to be 


## About this document

RFC 2119

SHOULD not only explain the what and how, but also the why.

SHOULD be self-explaining, although you might provide links for further
explanations.


## Table of contents

Project
- Scope
- Name
- Version
- Structure

Code
- Code style
- Core
  - f-strings
  - type hints
- Standard library
  - logging
  - enum
  - 
- External modules

Documentation
- Docstrings
- Type Hints
- README
- API Doc
- Changelog

Tests
- linting
- type checking
- coverage
- unittests
- automation

Packaging



## Project

### Scope

Consider the UNIX philosophy. Do one thing and do it well.
Do:
- instrument controller
Don#t. things that already exists, too large or to specific
- test framework
- 


## Name

You SHOULD choose a short, unique and meaningful name for your project. 
Have a look at the [Python Package Index](PyPI.org) and 
[pypi.rsint.net](pypi.rsint.net) if the name is already taken. 

Your package name (the import name) MUST be lowercase with optional underscores:
```
rsb_helloworld
```

The project name used everywhere else (repository name, project name in setup.py, 
project name used in documentation) MUST be the same, with underscores replaced
by dashes:
```
rsb-helloworld
```

Pip implicitly converts any separator to a dash. For git repositories, it is
common to use dashes as well. However, a dash cannot be part of a valid import
name in python, because it would be interpreted as a minus.

Discussion:

- Should all names use a common prefix like `rsb_` or `rs`? 
  Pros: 
  - A unique namespace avoids clashes with other projects. 
  - The user can already see when importing where the package comes from.
  Cons:
  - The name looks a bit bulky 
    (but you can still `import rsb_helloworld as helloworld`)
- If there is a prefix, what should it be? Prefixes that terminate in vowels
  are easier to pronounce and merge into a single word, like `aiohttp` 
  or `pytest`.
  But with our company name, it is difficult to come up with something similar,
  so we should use a separator?

### Version

You MUST identify each release with a version number following the
[Semantic Versioning](https://semver.org/) scheme, clauses 1-8:
```
Major.Minor[.Patch]
```
where Major, Minor and Patch are non-negative integers without leading zeroes.
You increment:
 - Major when you introduce backwards-incompatible API changes.
 - Minor when you add new public features without breakig the API.
 - Patch when you added bugfixes in a backwards-compatible manner.

This is compatible with [PEP440 - Version Numbering](https://www.python.org/dev/peps/pep-0440/).

You MAY use Major version zero to indicate that your package is still instable
and that the public API may change at any time. But don't be afraid to make a
first stable release `1.0` soon, because you probably won't run out of integers
for your Major version number.

You MUST tag the source code:
```
git tag -a v1.2.3 -m "Release version 1.2.3"
```
The version tag is usually prefixed with a `v`.

You MUST specifiy the package version in your project file, e.g. setup.py.

Discussion:

- What exactly is the public API of a python package?
  - Is it defined by the dosctrings in the `__init__.py`, each module and class?
  - Is it defined by the import hierarchy?
  - Is it defined by all names in the `__all__` list?
  - Is it defined by all packages, modules, functions, classes, methods and
    attributes without leading underscores?
- What if the package has one or several command-line interfaces? 
  Do they need separate versioning? 
- Where should the version number be defined? Should it also be part of the
  source code, and if so, how to single-source it?
  - The [Python Packaging Authority](https://packaging.python.org/guides/single-sourcing-package-version/)
    list several possibilities for setuptools.
  - Flit uses `__version__` inside `__init__.py` as the single source.
  - In Python 3.8, there is `importlib.metadata.version()`, so no need to put
    the version number in the source code?
   - 

  From vcs? necessary to add to code base, now that we have 
- Which extension to basic scheme allowed? (E.g. alpha and beta, release candidates, ...)


## Code

### Code style

Your code MUST comply with (PEP8)[https://www.python.org/dev/peps/pep-0008/], the
official python styleguide. Whereas PEP8 leaves room for interpretation, you SHOULD
use a checker like `pycodestyle` (which is part of `flake8`). You MAY use the 
autoformatter `black` to avoid any discussion about code style.

Discussion:
- The maximum line length is configurable even in black, which has a default of
  88 characters. Pycodestyle follows PEP8 and has a default of 79 characters.
  What should be choose?



## Documentation


## Docstrings

You should at least single-line for each public module and class.
google docstring convention. Noo need for Type hints (see next item).
can autogenerate APi documentation with sphinx, sphinx-apidoc and
sphinx-napoleon.
Choose between imperative or descriptive, but stick to it.
"Calculate" versus "Calculates.."

Single english phrase ending in a period. For all modules and public
classes, exceptions and functions.

Module dosctrings SHOULD contain a list of classes, exceptions and functions
Class docstring SHOULD include publich methods and attributes

Cl

Attributes
Methods


Args
Returns
Yields
Raises





## Type hints

You SHOULD use type hints.
Check with MYPY. 



## Documentation

You MUST write a README explaining purpose, setup and usage of your package.
You MAY use the (Temmplate)[].


You MUST document your code inline using docstrings.
You SHOULD use the Google style. It is more readable than the ReStructured Text 
(RST). *Add link to Google style* 

PEP257. 

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
