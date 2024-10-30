:orphan:

.. currentmodule:: time_str

.. _intro:

Installing time_str
===================

Prerequisites
-------------

time_str works with Python 3.9 or higher. Support for earlier versions of Python
is not provided. Python 2.7 or lower is not supported. Python 3.8 or lower is not supported.


.. _installing:

Installing
----------

.. note::

    For new features in upcoming versions, you will need to install the development version until a stable version is released. ::

        python3 -m pip install -U git+https://github.com/BobDotCom/time_str

    For Windows users, this command should be used to install the development version: ::

        py -3 -m pip install -U git+https://github.com/BobDotCom/time_str

You can get the library directly from PyPI: ::

    python3 -m pip install -U time_str

If you are using Windows, then the following should be used instead: ::

    py -3 -m pip install -U time_str

Virtual Environments
~~~~~~~~~~~~~~~~~~~~

Sometimes you want to keep libraries from polluting system installs or use a different version of
libraries than the ones installed on the system. You might also not have permissions to install libraries system-wide.
For this purpose, the standard library as of Python 3.3 comes with a concept called "Virtual Environment"s to
help maintain these separate versions.

A more in-depth tutorial is found on :doc:`py:tutorial/venv`.

However, for the quick and dirty:

1. Go to your project's working directory:

    .. code-block:: shell

        $ cd your-project
        $ python3 -m venv venv

2. Activate the virtual environment:

    .. code-block:: shell

        $ source venv/bin/activate

    On Windows you activate it with:

    .. code-block:: shell

        $ venv\Scripts\activate.bat

3. Use pip like usual:

    .. code-block:: shell

        $ pip install -U time_str

Congratulations. You now have a virtual environment all set up.
