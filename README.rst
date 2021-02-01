********
Time_Str
********

A package to convert user input into datetime.timedelta objects.

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

    >>> import time_str
    >>> time_str.convert('11 months 9days 1m 3 sec')
    datetime.timedelta(days=345, seconds=63)
    >>> time_str.convert('2 months 3w 1 d 5hour 3 min')
    datetime.timedelta(days=83, seconds=18180)