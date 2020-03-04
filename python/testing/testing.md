# Testing

## Unittest

Run all unit tests with top-level directory "example":
```
python -m unittest discover -s tests/unit -t example
```


## Pytest

### Test discovery

During development, an editable install via `pip install -e .` is recommended
(requires minimal setup.py).

Pytest works with different repository layouts. As long as the module names are
unique, the following test layout is supported:
```
setup.py
mypkg/
tests/
    test_unit.py
    test_integration.py
```

If you invoke pytest as `python -m pytest`, the only difference is that the
current working directory will be added to the python search path for modules.

You can define which tests to run the following ways:
- `pytest tests/`: run all tests in directory
- `pytest tests/test_core.py`: run all tests in file
- `pytest tests/test_core.py::test_connect`: run test with specific *node id*
- `pytest -k "client and not server"`: all tests that contain keyword in node id
- `pytest -m smoke`: all tests with certain marker

### Fixtures

Test functions can receive fixtures by naming them as an argument.
The fixture function of the same name is invoked and its result is passed to
the test.
The scope determines when exactly the fixture function is called.
Fixture functions can be registered with the `@pytest.fixture` decorator.
There are built-in fixtures, for example:
- `cache`: Cache object that persists between runs
- `pytestconfig`: configuration
- `tmpdir`: Temporary directory
- `capsys`: Capture stderr/stdout

### Markers

### Parameters

You can parametrize input arguments:
```python
@pytest.mark.parametrize("arg1", [1, 2, 3])
def test_sth(arg1):
    pass
```
For multiple arguments, either stack the decorators (which will lead to all
combinations of the parameters) or use a comma-separated string (or a list of
strings) for the arguments and a list of tuples for the values.
```python
@pytest.mark.parametrize("arg1,arg2", [(1, 2), (2, 3), (3, 4)])
def test_sth_else(arg1, arg2):
    pass
```

Of course, you can pass the actual values as a variable or by calling a
function that generates the values.

Pytest automatically generates node ids in the form `test_sth_else[1-2]` for
the individual tests. You can execute the test by their node ID or with the
keyword option.

You may specify additional metadata for a parameter tuple by wrapping it into
`pytest.param(1, 2, id="first", marks=pytest.mark.smoke)`.

You can also parametrize fixtures:
```python
@pytest.fixture(params=[0, 1], ids=["first", "second"])
def foo(request):
    return request.param

def test(foo)
```

The IDs are optional and appear in the node ID. It may also be a function that
is called on the parameter tuple, such as `str`.


### Command line arguments

**TODO**: pytest.adoption; complicated
