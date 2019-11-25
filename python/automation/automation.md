# Automation

## Test automation

With tox. Install tox:
```sh
pip install tox
```

You need to setup a `tox.ini` file or a section in the `setup.cfg` file.
Run all environments (that are defined in tox section as envlist):
```sh
tox
```

Run certain environments only:
```sh
tox -e <NAME>
```

Force recreation of virtual environment:
```sh
tox -r
```

You can increase verbosity with `tox -r` or decrease with `tox -q`.
