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

Pytest works with differnt repository layouts. As long as the module names are
unique, the following test layout is supported:
```
setup.py
mypkg/
tests/
    test_unit.py
    test_integration.py
```

### Fixtures

Test functions can receive fixtures by naming them as an argument.
The fixture function of the same name is invoked and its result is passed to
the test.
The scope determines when exactly the fixture function is called.
Fixture functions can be registered with the `@pytest.fixture` decorator.
There are built-in fixtures, fo example:
- `cache`: Cache object that persists between runs
- `pytestconfig`: configuration
- `tmpdir`: Temporary directory

### Markers

### Parameters

You can parametrize input arguments:
```
@pytest.mark.parametrize("arg1", [1, 2, 3])
def test_sth(arg1):
	pass
```
For multiple arguments, either stack the decorators or use a comma-separated
string (or a list of strings) for the arguments and a list of tuples for the 
values.

### Command line arguments

**TODO**: pytest.adoption; complicated
