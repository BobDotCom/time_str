:github_url: https://github.com/BobDotCom/time_str

Time_str Documentation
======================

A package to convert user input into datetime.timedelta objects.

|Docs badge| |Downloads badge|

.. |Docs badge| image:: https://readthedocs.org/projects/time_str/badge/?version=latest
   :target: https://time-str.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |Downloads badge| image:: https://static.pepy.tech/personalized-badge/bftools?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
   :target: https://pepy.tech/project/time_str
   :alt: Download Counter

PyPI: https://pypi.org/project/time_Str/

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
    print(time_str.convert('11 months 9days 1m 3 sec'))
    print(time_str.convert('2 months 3w 1 d 5hour 3 min'))

Manuals
-------

.. toctree::
   :maxdepth: 1

   api




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
