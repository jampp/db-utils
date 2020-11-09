=============
Running Tests
=============

Migratron tests can be executed ``pytest``

.. code-block:: bash

    pip install -r requirements-dev.txt
    pytest

But some tests require a PostgreSQL and some test a beeline connection.
To run the test that require PostgreSQL, you must set the ``MIGRATIONS_DB_TESTS``
environment variable. The database used must have ``test`` somewere on the name,
and it should be created.

For example:

.. code-block:: bash

    export MIGRATIONS_DB_TESTS=postgres://username:password@localhost/test_db
    pytest


To run the tests to use Hive, you should set the ``MIGRATIONS_HIVE_TESTS``
environment variable

.. code-block:: bash

    export MIGRATIONS_HIVE_TESTS='jdbc:hive2://localhost:10000/test'
    pytest
