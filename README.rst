********
Time_Str
********

|Mypy| |Pylint| |Black|

|Codecov| |Checks| |Lint| |Tests| |Pre-commit|

|PyPI| |Versions| |Docs badge| |Downloads badge| |GitHub|


A package to convert user input into datetime.timedelta objects.

.. |Mypy| image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: Checked with mypy
.. |Pylint| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
   :target: https://github.com/PyCQA/pylint
   :alt: linting: pylint
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. |Codecov| image:: https://codecov.io/gh/BobDotCom/time_str/branch/main/graph/badge.svg?token=MQGTWTBI5E
   :target: https://codecov.io/gh/BobDotCom/time_str
   :alt: Codecov
.. |Checks| image:: https://github.com/BobDotCom/time_str/actions/workflows/check.yml/badge.svg
   :target: https://github.com/BobDotCom/time_str/actions/workflows/check.yml
   :alt: Checks
.. |Lint| image:: https://github.com/BobDotCom/time_str/actions/workflows/lint.yml/badge.svg
   :target: https://github.com/BobDotCom/time_str/actions/workflows/lint.yml
   :alt: Type Check and Lint
.. |Tests| image:: https://github.com/BobDotCom/time_Str/actions/workflows/test.yml/badge.svg
   :target: https://github.com/BobDotCom/time_str/actions/workflows/test.yml
   :alt: Unit Tests
.. |Pre-commit| image:: https://results.pre-commit.ci/badge/github/BobDotCom/time_str/main.svg
   :target: https://results.pre-commit.ci/latest/github/BobDotCom/time_str/main
   :alt: pre-commit.ci status

.. |PyPI| image:: https://img.shields.io/pypi/v/time_str.svg?logo=pypi&color=yellowgreen&logoColor=white
   :target: https://pypi.python.org/pypi/time_str
   :alt: PyPI version info
.. |Versions| image:: https://img.shields.io/pypi/pyversions/time_str.svg?logo=python&logoColor=white
   :target: https://pypi.python.org/pypi/time_str
   :alt: PyPI supported Python versions
.. |Docs badge| image:: https://readthedocs.org/projects/time_str/badge/?version=latest
   :target: https://time_str.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. |Downloads badge| image:: https://static.pepy.tech/personalized-badge/time_str?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
   :target: https://pepy.tech/project/time_str
   :alt: Download Counter
.. |GitHub| image:: https://img.shields.io/github/v/release/BobDotCom/time_str?include_prereleases&label=Latest%20Release&logo=github&sort=semver&logoColor=white
   :target: https://github.com/BobDotCom/time_str/releases
   :alt: Latest release

PyPI: https://pypi.org/project/time-str/

Docs: https://time-str.readthedocs.io/en/latest/

Installation
############

You can install released versions of time_str from the Python Package Index via pip or a similar tool:

**Stable Release:** ``pip install time_str``

**Working Version:** ``pip install git+https://github.com/BobDotCom/time_str.git``

Usage
#####
.. code-block:: python

    import time_str
    converter = Converter('11 months 9days 1m 3 sec')
    print(converter.timedelta_precise())
    print(converter.datetime_precise())
