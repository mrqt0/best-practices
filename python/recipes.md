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

#### General

- `x or y` return `x` if `x` is *truthy* (evaluates to `True`), else is it
  returns `y`.

#### Special methods

- You can overwrite `__bool__` to define the truthiness of your class, i.e. how
  it behaves in statements like `if`, or with operands `and`, `or`, `not`.
  If `__bool__` is not defined, `__len__` is compared to zero.
- Binary operators bind to the left. You can define the reversed operators like
  `__radd__` as fallbacks, if `__add__` is not defined.
- The augmented assignment operators `__iadd__` are for `x *= y`. If it is not
  implemented, Python falls back to `__add__`. The `i` stands for inplace.
- An object becomes iterable just by defining `__getitem__`; keys will be the
  sequence of integers.
- If you specify `__len__`, you can iterate over the `reversed` object. However,
  forward iteration will not stop at the length.
- With `__contains__`, you define the behavior for the `in` operator.
  The fallback is a sequential scan by iteration.


#### Data structures

Sequences

- lists: mutable and mixed-type.
- tuples: immutable, mixed-type
- `collections.namedtuple`: tuples with field names
- slicing: The `start:stop:stride` syntax is only valid within brackets and
  evaluates to `.__getitem__(slice(start, stop, stride))`. You can also store
  slice objects for later usage.
- You can also assign to slices, but the right side must be an iterable:
  `a[5:10] = [10]`
- `.sort` sorts in-place, `sorted` returns a new object. By convention,
  in-place functions return `None`. Both accept `key` callable that transforms
  the elements and `reverse` flag.
- `bisect.bisect(seq, value)` performs a binary search on a sorted sequence to
  return the index where the value should be inserted. `bisect_left` returns
  the index to the *left* of the existing item. `insort` and `insort_right`
  insert the element at the right position. All functions take `lo` and `hi` to
  specify a subset of the sequence by index.
- `array.array` for lean C-style arrays of numeric data. They support `tofile`
  and `fromfile` methods.
- The `memoryview()` built-in class lets you handle buffery like array or bytes
  without actually copying the underlying bytes.
- Use `collections.deque` for lists with efficient access at both ends (no need
  to shift the whole sequence) and limited size feature.

Iterable unpacking: starred expression can capture "rest" in list. It may
appear at any position.
```
a, b, *rest = range(5)
```

### Mappings

- Most functions that take dict check argument for `keys()` method. If it
  doesn't exist, it treats argument as iterator over tuples.
- Get default if key not found: `d.get(key, default)`
- Get default and set value if key not found: `d.setdefault(key, [])`
- Provide default factory for all missing keys: `collections.defaultdict(list)`
  (only invoked for bracket access or `__getitem__`, not get e.g.)
- You can also add a `__missing__` method which is called in case a key is not
  found (but only for `__getitem__`, not `__contains__` or `get`).
- `dict.keys()` and `dict.values()` are view objects. They provide fast
  containment checks.
- `collections.ChainMap`: fast lookup in multiple dicts (e.g. variable lookup
  in multiple scopes).
- `collections.Counter`: counts occurrence of elements, can be updated with
  new sequences and provides `most_common(num)` method
- `Mapping.update` and `dict` constructor can also take keyword arguments.
  Update calls `__getitem__` under the hood.
- `types.MappingProxyType` returns a dynamic, but read-only view of a dict.
  A class' dict is such a mappingproxy.

How dicts work:

- Keys to a dict must be hashable, i.e.:
  - have a `__hash__` method that never changes during lifetime
  - have a `__eq__` that returns true for values with the same hash value
- This implies that you must never implement hash for mutable equality checks.
- Dict lookup:
  1. `hash(key)`
  2. Take least significant bits
  3. Lookup bucket at this position.
     - If it is empty: raise KeyValue or insert item.
     - If it is used: Compare keys. If they match: return item. If not:
       Modify hash and repeat process to resolve collision.
- The dict size is increased when the table becomes more crowded, to reduce
  collisions. Dicts waste memory for two reasons: a list of dicts stores the
  keys ever time, and the table is intentionally parse. You may either use
  tuples, or `__slots__` for classes so tuples are used internally instead of
  dicts.
- *Note*: This explains why dicts were unordered in earlier python versions.

### Strings and bytes

- Unicode: there are up to 1,114,111 *code points*, about 10% of which have
  characters assigned in Unicode 6.3
- A character encoding like UTF-8 assigns code points to bytes. This process is
  called encoding (from `str` to `bytes`), the reverse process is called
  decoding (`bytes` to `str`).
- Elements of `bytes` are integers in `range(256)`. Slices of any length are
  `bytes`. `bytearray` is a mutable `bytes`.
- `bytes` are represented by ASCII characters in the printable range `[ -~]`,
  `\t\r\n\\` or the corresponding hex value, e.g. `\x00`.
- You can create `bytes` from:
  - `bytes.fromhex("ff 01")`
  - iterable of integers in `range(256)`
  - string and encoding
  - object that implements buffer protocol (`bytes`, `bytearray`, `memoryview`,
    `array.array`). Note that this copies the bytes, unlike `memoryview`
- You can pass `str.encode("utf-8", errors="ignore")` or `"replace"` to handle
  characters that are not part of codec. Otherwise, `UnicodeEncodeError` is
  raised.
- It also works the other way around: `errors="replace"` use the official
  unicode replacement character.
- You should always pass encoding argument when opening text files: otherwise
  Windows typically assumes "cp1252", which is `locale.getpreferredencoding()`.
  This setting also affects when writing streams to files.



### Standard library

- Take random element: `random.choice([1, 2])`


#### Strings

- Use `str.translate(mapping)` to translate multiple characters
- Print four-byte unicode characters: `"\U0001F4A9"` with uppercase `U` or `chr(0x1F4A9)`
- See [https://docs.python.org/3/howto/unicode.html] for more info

### File operations

Unpack all archives:
```py
def unpack(root, delete_archive=False):
    for path in Path(root).glob("**/*.zip"):
        logging.info(f"Unpacking '{str(path)}'")
        with zipfile.ZipFile(path) as archive:
            archive.extractall(path.with_suffix(""))
        if delete_archive:
            path.unlink()
```

## To Do

- functools
- itertools
