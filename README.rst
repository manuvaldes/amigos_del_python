pyramide
========  

|license| |python version| |build-status| |docs| |coverage| |pypi package|

.. |license| image:: https://img.shields.io/github/license/manuvaldes/amigos_del_python.svg
.. |build-status| image:: https://travis-ci.org/manuvaldes/amigos_del_python.svg?branch=master
    :target: https://travis-ci.org/manuvaldes/pyramide
.. |docs| image:: https://readthedocs.org/projects/amigos_del_python/badge/?version=latest
    :target: http://pyramide.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |coverage| image:: https://coveralls.io/repos/github/manuvaldes/amigos_del_python/badge.svg?branch=master
    :target: https://coveralls.io/github/manuvaldes/pyramide?branch=master
.. |pypi package| image:: https://badge.fury.io/py/amigos_del_python.svg
    :target: https://badge.fury.io/py/pyramide
.. |python version| image:: https://img.shields.io/pypi/pyversions/amigos_del_python.svg
   :target: https://pypi.python.org/pypi/pyramide

pyramide es un simple crawler basado en crawlerino

install and test
=======================

install from pypi
********************

using pip:

.. code-block:: bash

    $ pip install pyramide

dev install
****************

There is a makefile in the project root directory:
    
.. code-block:: bash

    $ make dev

Using pip, the above is equivalent to:

.. code-block:: bash

    $ pip install -r requirements-dev.txt                                             
    $ pip install -e .

run the tests
******************

Use the makefile in the project root directory:

.. code-block:: bash

    $ make test

This runs the tests generating a coverage html report

build the doc
******************

The documentation is made with sphinx, you can use the makefile in the
project root directory to build html doc:

.. code-block:: bash

    $ make doc

Documentation
=======================

Documentation on `Read The Docs`_.

Meta
=======================

manuvaldes - manuvaldes@gmail.com

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

https://github.com/manuvaldes


.. _Read The Docs: http://pyramide.readthedocs.io/en/latest/

