# Automation with tox

## Overview

Install tox:
```sh
pip install tox
```
You may install it into a virtual environment and create an alias.

You need to setup a `tox.ini` file or a `[tox:tox]` section in the `setup.cfg`
file. Run all environments:
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

You can increase verbosity with `tox -v` or decrease with `tox -q`.


## Environments

Tox is based on virtual environments. For each "step" (actually called an
environment), tox creates a separate virtual environment, installs the
dependencies and runs the command.

If you simply invoke `tox`, tox runs all the environments defined in `envlist`
```ini
[tox]
envlist=lint,test
```

The actual environments are defined in the `[testenv:<name>]` sections.
Common defaults are directly defined under `[testenv]`.
```ini
[testenv]
download = true

[testenv:lint]
deps = pylint
commands = pylint
```

You do not have to create virtual environments manually, but can generate
environments from "factors" and use the factors as conditions on the settings:
```ini
[tox]
envlist = py{27,37}-{lint}

[testenv:lint]
deps =
  py27: pylint
  py37: black
commands =
  py27: pylint
  py37: black --check

```

You can list the environments with `tox -l`.


## Dependency Management

### Tox

You can ensure a certain tox version:
```ini
[tox]
minversion = 3.4.0
requires = tox-venv
```

### Python

The python version for each environment can be specified by name or by path
with `basepython`. Otherwise it is deduced from the environment name.


### Dependencies

Set `download=true` to upgrade pip, setuptools and virtual environments.
If your filesystem cannot handle symlinks, use `alwayscopy=true`.
Tox installs the dependencies defined in `deps` with the install command
defined in `install_command=python -m pip install {opts} {packages}`.
This also applies to the package under test.
To force recreation of the environments, use `recreate=true`.


### Package under test

- `skipsdist=true`: skip the packaging step (e.g. for applications without
  setup.py, global settings).
- `use_develop=true`: Install in editable mode (env settings)
- `skip_install=true`: Do not install package (env settings)


## Substitutions

You can access variables via curl braces, e.g. `{distdir}`.
Some variables are predefined. Environmental variables can be accessed via
`{env:KEY}` and optional default value `{env:KEY:DEFAULT}`. Another special
value are the positional arguments passed to tox: `{posargs:DEFAULT}.`

After two dashes, you can specify additional options which are passed to
a test commands' posargs: `tox -- --opt val`.

Finally, you can use values from other sections: `[NAME]KEY`

## Execution

- `ignore_errors=true`: Ignore non-zero exit code of command.
- `- pylint`: Add dash to ignore non-zero exit code of single command.
- `commands_pre`: Commands are only run if these commands succeed.
- `commands_post`: Commands are always run.
