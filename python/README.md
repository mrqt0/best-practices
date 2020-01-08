# Python Best Practices

## To Do

- relpython timer: checkout contextlib.ContextDecorator
  or different ways of tic/toc + contextmanager + decorator


- [ ] Set up linting, autocompletion in sublime text

- [ ] pathtools
- [ ] cli
- [ ] Check out article on async init patterns: http://as.ynchrono.us/2014/12/asynchronous-object-initialization.html
  - dependency injection: `__init__` consumes objects; there is additional async
    factory class method
  - classmethod for creation
  - separate module-level method for creation
  - context manager
  - check out async-dgram: https://pypi.org/project/asyncio-dgram/
- [ ] Check out functools dispatch pattern

## Table of Contents

- [Guidelines](guidelines.md)
- Topics
  - packaging: setuptools, flit, poetry, python import system, ...
  - testing: unittest, pytest, tox
  - plotting: matplotlib
  - documentation: sphinx
  - automation: tox
  - command-line: argparse
  - concurrency: asyncio
  - web:
- [Snippets](snippets.md)
  - logging
  - bytes/int/string/hex conversions
  - regex
  - importlib
  - metaclasses
  - singletons
  - introspection
- Reading: list of useful links


While the guidelines should be concise and give one single recommendation, the
topics can explore different aspects more in depth, as well as alternatives.

The snippets are for quick look-up. They be me moved to a topic-based folder
later.


## Setting up Sublime Text 3

Useful syntax-specific settings:
```json
    // maximum line length for dosctrings and code
    "rulers": [72, 79]
```

## IDE features with Anaconda

Install via package control:
- Press `Ctrl + Shift + P`
- Type `Install Package Control` and
- Type `Package Control: Install Package`
- Search for `Anaconda`. Works out of the box.

Features:
- Autocompletion
- Go to definition: `Ctrl+Alt+G`
- Find usages. `Ctrl+Alt+F`
- Show documentation: `Ctrl+Alt+D`

Fine tune settings:
- Go to `Preferences` -> `Package Settings` -> `Anaconda` (default or user)
- Disable linting:
```json
    "anaconda_linting": false,
    "pep8": false,
```
- Set the python interpreter (can point to venv):
```json
    "python_interpreter": "path/to/python",
```


## Linting with SublimeLinter-flake8

- Precondition: install flake8
- Either make sure flake8 is available on the path, or specify the `python`
  or `executable` SublimeLinter settings
- Install SublimeLinter via package control
- Optional settings:
```json
{
    "styles": [
        {
            "mark_style": "squiggly_underline"
        }
    ],
    "lint_mode": "load_save"
}
```


## General Python Programming

With `__all__`, you can limit what is importable with `from module import *`.
It also influences IDEs and documentation tools like sphinx.


### Tricks and Patterns

- Use context managers for setup and teardown, either class-based or
  function-based.
  Also works for asynchronous enter and exit functions.
  Inherit from `contextlib.ContextDecorator` so the class can also be used as
  a decorator.
- Use `itertools`:
  - `islice` to take only part of iterator
  - `dropwhile` to skip first elements based on condition
- Use `str.translate(mapping)` to translate multiple characters

#### general

- [Nick Coghlan: Considering Python's target audience](
  http://www.curiousefficiency.org/posts/2017/10/considering-pythons-target-audience.html):

#### Asyncio

- [Armin Ronacher](https://lucumr.pocoo.org/2020/1/1/async-pressure/):
  about backpressure and flow control. He says it is probably a mistake that
  you can't await on `writer.write()`.

#### Packaging

- [James Bennett: A Python Packaging Carol](
  https://www.b-list.org/weblog/2020/jan/05/packaging/):
  Python packaging is actually not that bad. You need to distinguish
  distribution, installation and environment handling (which is not so bad).
- [Glyph: Python Packaging Is Good Now](
  https://glyph.twistedmatrix.com/2016/08/python-packaging.html):
  Talks about history until time article (2016) and how much it has improved.
- [Nick Coghlan: The Python Packaging Ecosystem](
  http://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html):



#### Pytest

- [Martin Heinz: Pytest Features, That You Need in Your (Testing) Life](
  https://martinheinz.dev/blog/7)


### Libraries and Applications

- [PyOxidizer](https://pyoxidizer.readthedocs.io/en/latest/index.html):
  Create stand-alone applications
- [pipx]() Install python packages into isolated and globally accessible
  environment


### Further Reading

- [Code Style](https://docs.python-guide.org/writing/style/)
- [Tricks](https://martinheinz.dev/blog/1)
- [Design Patterns](https://stackabuse.com/design-patterns-in-python/)


## Resources

- [Moshe Zadka](https://opensource.com/article/19/11/document-python-sphinx)
- [Al Sweigart]()
- [Steve Dower]: Works at Microsoft, brought Python to the Windows Store
- [Armin Ronacher](https://lucumr.pocoo.org/about/): Creator of Flask etc.
- [Glyph](): Author of Twisted
