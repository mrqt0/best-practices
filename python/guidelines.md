# Python Guidelines

> R&S Guidelines for writing Python Packages

Imagine you have written some Python code you consider useful for other people
within the company. You would like to share it as a pip-installable library,
but you don't know where to start. Writing Python code is easy, but the
ecosystem can be a bit overwhelming: Information is scattered, outdated,
too general to be really helpful and sometimes even contradictory.

This guide wants to bring you from python scripts on your local drive to
high-quality packages on pypi.rsint.net.
It is targeted at libraries for build, test and process automation inside
Rohde & Schwarz. However, some parts may be applicable to applications and
productive code as well.

TODO: link to inneRSource

Following these guidelines has several benefits:
- You do not have to figure out everything yourself.
- You can use predefined templates, project files and CI pipelines.
- In case of problems, you can benefit from the experience of others.
- Users will quickly be familiar with your package.
- Users know which quality standards you adhere to.
- TODO: You might have the chance of centralized funding

TODO: Links to other projects


## About this document

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).
- MUST, SHALL, REQUIRED: absolute requirement
- MUST NOT, SHALL NOT: absolute prohibition
- SHOULD, RECOMMENDED: there may be reasons to ignore item
- SHOULD NOT, NOT RECOMMENDED: there may be reasons when item is acceptable
- MAY, OPTIONAL: truly optional

SHOULD not only explain the what and how, but also the why.

SHOULD be self-explaining, although you might provide links for further
explanations.


## Table of contents

- [Project](#project)
  - [Scope](#scope)
  - [Name](#name)
  - [Version](#version)
  - [Structure](#structure)
- [Code](#code)
  - Code style
  - Built-ins and standard library
  - External modules
- [Documentation](#documentation)
  - [Docstrings](#docstrings)
  - [Type Hints](#type-hints)
  - [Read Me](#readme)
  - [API Doc](#api-doc)
  - [Changelog](#changelog)
- [Tests](#tests)
  - [Linting](#linting)
  - [Type checking](#type-checking)
  - [Unit tests](#unittests)
  - [Coverage](#coverage)
  - [Automation](#automation)
- [Distribution](#distribution)


Responsibility
Version control

## Project

### Scope

Consider the UNIX philosophy. Do one thing and do it well. Work together.
Do:
- instrument controller
Don#t. things that already exists, too large or to specific
- test framework
-


### Name

You SHOULD choose a short, unique and meaningful name for your project.
Have a look at the [Python Package Index](PyPI.org) and
[pypi.rsint.net](pypi.rsint.net) if the name is already taken.

The project name (repository name, project name in setup.py, project name used
in documentation, etc.) MUST be lowercase with optional dashes:
```
rsb-helloworld
```
Dashes are common for git repositories. Pip also implicitly converts any
separator to a dash. However, a dash cannot be part of a valid import name in
python, because it would be interpreted as a minus. Your package name (name of
the directory where the source code lives) MUST therefore use an underscore
instead of a dash:
```
rsb_helloworld
```



### Version

You MUST identify each release with a version number following the
[Semantic Versioning](https://semver.org/) scheme, clauses 1-8:
```
Major.Minor[.Patch]
```
where Major, Minor and Patch are non-negative integers without leading zeros.
You increment:
 - Major when you introduce backwards-incompatible API changes.
 - Minor when you add new public features without breaking the API.
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

You MUST specify the package version in your project file, e.g. `setup.py`.

### Structure

You MUST put your project under version control on Gitlab. You SHOULD stick
to the following basic structure for your repository:


Minimal:
```
my-project/
├── src/
│   └── my_project.py
├── tests/
│   └── test_my_project.py
├── README.md
└── setup.py
```

Optional:
```
my-project/
├── data/
│   ├──
│   └──
├── docs/
│   ├── conf.py
│   └── index.rst
├── src/
│   └── my_project.py
│       ├── __init__.py
│       ├── __main__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── integration/
│   │   └── test_my_project.py
│   └── unit/
│       ├── test_module1.py
│       └── test_module2.py
├── .gitignore
├── .gitlab-ci.yml
├── pyproject.toml
├── README.md
├── setup.py
├── setup.cfg
├── tox.ini
└── setup.py
```
- The source code lives inside its own directory.
- The tests . Tox.ini configuration and automation.
- Documentation: README.md and docs/
- Project files. For packaging and other tools configs.
- CONTRIBUTING, LICENSE and CHANGELOG can be inside README.

changelog
yaml



## Code

### Code style

Your code MUST comply with [PEP8](https://www.python.org/dev/peps/pep-0008/),
the official python style guide. Whereas PEP8 leaves room for interpretation,
you SHOULD use a checker like `pycodestyle` (which is part of `flake8`). You
MAY use the autoformatter `black` to avoid any discussion about code style.

### Built-ins and Standard library

Mdoern python code



- Core
  - f-strings
  - type hints
  - exceptions
- Standard library
  - logging
  - enum
  - dataclasses

### Third-party libraries



## Documentation

### Docstrings

Docstrings as described in [PEP 257](https://www.python.org/dev/peps/pep-0257/)
are the standard for documenting Python code.
The built-in `help()` function, IDEs and API documentation generators all make
use of docstrings. You can even access them during runtime via the `__doc__`
attribute.

You MUST write at least a one-line docstring for each public package, module,
class, exception, method and function. You SHOULD follow these conventions:
- Surround the docstring by triple double quotes on the same line as the text.
- Limit the docstrings to 72 characters.
- Write a single English phrase, starting in a capital letter and ending in a
  period.
- Choose either imperative ("Calculate...", preferred) or descriptive
  ("Calculates...") style and be consistent throughout the project.

Example:
```py
def add(a, b):
    """Calculate the sum of two values."""
    return a + b
```

For non-trivial cases, you SHOULD write multi-line docstrings. You SHOULD use
the [Google style](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings),
which is more human-friendly than reStructuredText (RST) and less verbose than
the Numpy style.
Most tools can handle Google docstrings, for example the
[PyCharm IDE](https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html)
and the Sphinx documentation generator with help of the
[Napoleon extension](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html).
Check out the [Napoleon examples](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
for reference. You SHOULD follow these conventions:
- Start with summary line, separated by a blank line from the rest.
- Put more detailed description of purpose and behavior into the following
  paragraphs, each separated by a blank line.
- Add the relevant [sections](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#docstring-sections), each separated by a blank line. They
  consist of a section heading and an indented list of values.
- Finish with triple double quotes on a separate line, followed by a blank line
  before the code starts.


### Type hints

You SHOULD use type hints.
Check with MYPY.


### README

You MUST write a README explaining purpose, setup and usage of your package.
You MAY use the (Template)[].



## Tests

### Static Analyis

Static code analysis often included with stylistic checks.
flake8 and pylint. mypy

### Type Checking


### Tests

Yout MUST write unit tests.


### Coverage

**TODO**

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
or passed as command line arguments:
```ini
ignore = E305
exclude = .git,__pychache__
max-line-length = 90
```



## Typing

MyPy: most used, by google
Alternatives:
- pyright: Microsoft
- pyre: Facebook
- pytype: Google
