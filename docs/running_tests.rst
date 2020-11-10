=============
Running Tests
=============

Migratron tests can be executed ``pytest``

.. code-block:: bash

    pip install -r requirements-dev.txt
    pytest

Some tests require a PostgreSQL and others a beeline connection.
To run the tests that require PostgreSQL, you must set the ``MIGRATIONS_DB_TESTS``
environment variable. The database used must have ``test`` somewhere in the name,
and it should be created.

For example:

.. code-block:: bash

    export MIGRATIONS_DB_TESTS=postgres://username:password@localhost/test_db
    pytest


To run the tests that use Hive, you should set the ``MIGRATIONS_HIVE_TESTS``
environment variable

.. code-block:: bash

    export MIGRATIONS_HIVE_TESTS='jdbc:hive2://localhost:10000/test'
    pytest
