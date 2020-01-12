# Recipes

> Tricks, snippets, recipes etc.

Everything that is common enough to appear again, but too uncommon to be
remembered.

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
