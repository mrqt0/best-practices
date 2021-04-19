# Python Best Practices

## To Do

- realpython timer: checkout contextlib.ContextDecorator
  or different ways of tic/toc + contextmanager + decorator

- [ ] put terminal cfg here
- Reorganize documents:
  -
  - resources
    - articles
    - projects
    - people
  - tricks / patterns / ...
  - guidelines


- [ ] pathtools
- [ ] functools
  - check out dispatch pattern
- [ ] itertools
- [ ] Regex: group access, backreference, lazy quantifiers, lookahead, look behind
- [ ] Datetime
- [ ] cli
- [ ] Check out article on async init patterns: http://as.ynchrono.us/2014/12/asynchronous-object-initialization.html
  - dependency injection: `__init__` consumes objects; there is additional async
    factory class method
  - classmethod for creation
  - separate module-level method for creation
  - context manager
  - check out async-dgram: https://pypi.org/project/asyncio-dgram/

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
- [Recipes](recipes.md): Tricks, snippets and recipes for things that are hard
  to memorize.
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

Resources:
- https://blog.usejournal.com/ultimate-sublime-for-python-5c531224421b

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
- Find usages: `Ctrl+Alt+F`
- Show documentation: `Ctrl+Alt+D`
- Autoformat: `Ctrl+Alt+R`
- Fill function arguments: `Tab`

Fine tune settings:
- Go to `Preferences` -> `Package Settings` -> `Anaconda` (default or user)
- Disable linting:
```json
    "anaconda_linting": false,
    "pep8": false,
    "suppress_word_completions": true,
    "suppress_explicit_completions": true,
}

```
- Set the python interpreter (here: point to venv in project file):
```json
    "python_interpreter": "$folder/.venv/Scripts/python.exe",
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
