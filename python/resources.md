# Resources

Links to articles I read. Of course it would be best to provide a short summary.

## Articles

### Python Language

- [Nick Coghlan: Considering Python's target audience](
  http://www.curiousefficiency.org/posts/2017/10/considering-pythons-target-audience.html):
  Talks about different user groups and use cases of Python. Highlights the
  importance of not forgetting about the "silent" teaching and data science
  community.

### Code style

- [Python Guide: Code Style](https://docs.python-guide.org/writing/style/)
- [List of rules for flake8](https://lintlyci.github.io/Flake8Rules/)


### Recipes

- [Martin Heinz: Python Tips and Trick, You Haven't Already Seen](
  https://martinheinz.dev/blog/1)
- [Darinka Zobenica: Design Patterns in Python (Series)](
  https://stackabuse.com/design-patterns-in-python/)
- [Brandon Rhodes: Python Patterns (Series)](https://python-patterns.guide/)


### Asyncio

- [Lynn Root: Advanced Asyncio: Solving Real World Production Problems (video)](
  https://www.youtube.com/watch?v=yKfenooKl6M)
- [Stefan Scherfke: Advanced asyncio testing](
  https://stefan.sofa-rockers.org/2016/03/10/advanced-asyncio-testing/):
- [Armin Ronacher: I'm not feeling the async pressure](
  https://lucumr.pocoo.org/2020/1/1/async-pressure/):
  about backpressure and flow control. He says it is probably a mistake that
  you can't await on `writer.write()`.
- [Yeray Diaz: asyncio for the working Python developer](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e#.ft56qol06)
- [Chris Medina: Threaded asynchronous magic and how to wield it](
  https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32#.8qk30tq31)
- [Chris Medina: Asyncio in 3.7](https://tryexceptpass.org/article/asyncio-in-37/)


### Documentation

Type Hints:
- [Bernat Gabor: the state of type hints in Python](
  https://www.bernat.tech/the-state-of-type-hints-in-python/)
- [Al Sweigart: Type Hints for the Busy Python Programmer](https://inventwithpython.com/blog/2019/11/24/type-hints-for-busy-python-programmers/)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

Sphinx:
- [Moshe Zadka](https://opensource.com/article/19/11/document-python-sphinx)

### Testing

Pytest:
- [Martin Heinz: Pytest Features, That You Need in Your (Testing) Life](
  https://martinheinz.dev/blog/7)
Tox:
- [Ionel Cristian Mărieș: Tox tricks and patterns](
  https://blog.ionelmc.ro/2015/04/14/tox-tricks-and-patterns/)
- [tox on python bytes 44](https://pythonbytes.fm/episodes/show/44/pip-install-malicious-code)
- [tox changedir instead of src](https://pythonbytes.fm/episodes/show/138/will-pyoxidizer-weld-shut-one-of-python-s-major-gaps)

### Packaging

Quick start:
- [Jie Feng: A Simple Guide for Python Packaging](
  https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5#.b9ww4h4xt)
- [Hynek Schlawack: Sharing Your Labor of Love: PyPI Quick and Dirty](
  https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)

Toolchains:
- [Stefan Scherfke: Python packaging with gitlab and conda](https://stefan.sofa-rockers.org/2019/04/18/python-packaging-gitlab-conda/)
  - Use gitlab runner instead of tox to run locally
  - Use docker inside docker to use images from other gitlab projects
  - prefix packages with `own`
  - Use master and develop branch to deploy into stable and staging channel
  - Version number is `$GIT_DESCRIBE_TAG.$GIT_DESCRIBE_NUMBER`

Historical overviews:
- [James Bennett: A Python Packaging Carol](
  https://www.b-list.org/weblog/2020/jan/05/packaging/):
  Python packaging is actually not that bad. You need to distinguish
  distribution, installation and environment handling (which is not so bad).
- [Glyph: Python Packaging Is Good Now](
  https://glyph.twistedmatrix.com/2016/08/python-packaging.html):
  Talks about history until time article (2016) and how much it has improved.
- [Nick Coghlan: The Python Packaging Ecosystem](
  http://www.curiousefficiency.org/posts/2016/09/python-packaging-ecosystem.html)
- [Andrew Pinkham: Python's New Package Landscape](
  http://andrewsforge.com/article/python-new-package-landscape/)
- [Dustin Ingrim: Inside the Cheeseshop: How Python Packaging works (Video)](
  https://www.youtube.com/watch?time_continue=1&v=AQsZsgJ30AE&feature=emb_logo)

Src-directory:
- [Testing your python package as installed by Per Ganssle](https://blog.ganssle.io/articles/2019/08/test-as-installed.html)
- See [python bytes 22](https://pythonbytes.fm/episodes/show/22/pythonpath-considered-harmful)
- https://hynek.me/articles/testing-packaging/
- See [python bytes 15](https://pythonbytes.fm/episodes/show/15/digging-into-python-packaging)
- https://python-packaging.readthedocs.io/en/latest/
- [Brian Skinn: setuptools and pyproject.toml](https://bskinn.github.io/My-How-Why-Pyproject-Src/)

About PEP 417 and 418:
- [Test & Code with Brett Cannon](https://testandcode.com/52)


## People

- [Moshe Zadka](https://opensource.com/article/19/11/document-python-sphinx)
- [Al Sweigart](https://alsweigart.com/): Author of "Automate the boring stuff
  with Python", also uses games for education
- [Steve Dower]: Works at Microsoft, brought Python to the Windows Store
- [Armin Ronacher](https://lucumr.pocoo.org/about/): Creator of Flask etc.
- [Glyph](https://glyph.twistedmatrix.com/): Author of Twisted
- [Mahmoud Hashemi](https://github.com/mahmoud): Author of boltons, worked at
  Paypal
- [Paul Ganssle](https://blog.ganssle.io/): Maintainer of setuptools and
  dateutils, core developer, works at Google
- [Bernat Gabor](https://www.bernat.tech/): Maintainer of tox and virtualenv,
  works at Bloomberg
- [Hynek Schlawack](https://hynek.me/): Maintainer of attrs
- [Ionel Cristian Mărieș](https://blog.ionelmc.ro/): Maintainer of pytest-cov



## Projects

- [fire](https://github.com/google/python-fire): convert functions and object
  to cli
- [boltons](https://github.com/mahmoud/boltons): Utility extensions to the
  standard library
- [PyOxidizer](https://pyoxidizer.readthedocs.io/en/latest/index.html):
  Create stand-alone applications
- [pipx]() Install python packages into isolated and globally accessible
  environment
- [aiomas](https://aiomas.readthedocs.io/en/latest/index.html): RPC and multi-
  agent library similar to remex, written in asyncio (Stefan Scherfke)


