# Sphinx

Install Sphinx:

```sh
pip install sphinx
```

From your project root directory, create a `docs` directory:
```sh
mkdir docs
cd docs
```

Initialize the docs directory:
```sh
sphinx-quickstart
```

This will ask you for configuration. Make sure that you decide to use separate
source and build directories. There will be a `source/conf.py` file. Also make
sure that you create a Makefile and a make.bat for Windows.

When prompted, add the autodoc extension. Add the napoleon extension, which
does not need to be installed for Sphinx >= 1.3:
```py
extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autodoc']
```

You might need to uncomment the lines where the python path is modified:
```py
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

Create API documentation stubs:
```sh
sphinx-apidoc -f -o source <path/to/source>
```

Generate documentation:
```sh
make html
```

Open in browser:
```sh
start build/html/index.html
```

To Do:
- Configure Napoleon plugin
