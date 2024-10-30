:orphan:

.. _quickstart:

.. currentmodule:: time_str

Quickstart
==========

This page gives a brief introduction to the library. It assumes you have the library installed.
If you don't, check the :ref:`installing` portion.

Usage
-----

.. code-block:: python

    import time_str
    converter = IntervalConverter('11 months 9days 1m 3 sec')
    print(converter.timedelta_precise())
    print(converter.datetime_precise())
