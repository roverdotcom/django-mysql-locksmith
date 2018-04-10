========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/django-warlock/badge/?style=flat
    :target: https://readthedocs.org/projects/django-warlock
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/roverdotcom/django-warlock.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/roverdotcom/django-warlock

.. |codecov| image:: https://codecov.io/github/roverdotcom/django-warlock/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/roverdotcom/django-warlock

.. |version| image:: https://img.shields.io/pypi/v/django-warlock.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-warlock

.. |commits-since| image:: https://img.shields.io/github/commits-since/roverdotcom/django-warlock/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/roverdotcom/django-warlock/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-warlock.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-warlock

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-warlock.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-warlock

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-warlock.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-warlock


.. end-badges

A Django backend for encforing lockless migrations with MySQL

* Free software: BSD 3-Clause License

Installation
============

::

    pip install django-warlock

Documentation
=============

https://django-warlock.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
