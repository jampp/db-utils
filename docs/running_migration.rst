==================
Running Migrations
==================

.. contents::
    :local:

``Migratron`` is a very simple migration system:

Given a path where the migrations files are, it will check which have not been
applied. For this, it has a custom table on the database called ``db_migrations``
which has the path of the executed files and when they were executed.

First time
==========

If it is the first time you are running the migration against the database,
make sure to run the migrations with the ``--just-base-schema`` to create the ``db_migrations``
table. Check :ref:`connect_to_the_database`

.. code-block:: console

    migratron initialize --just-base-schema --migrations-path PATH_TO_MIGRATION_FILES


Once that the initial ``migratron`` setup has been done you could just run the
migrations as usual

Running Missing Migrations
==========================

To update the database information, you must use:

.. code-block:: console

    migratron migrate --migrations-path PATH_TO_MIGRATION_FILES

Run:

.. code-block:: console

    migratron migrate --help

to get more information on the required parameters, or check `Connect to the Database`_


Working With Branches
=====================

``Migratron`` doesn't take into account the different branches.
So there are two solutions:

1. Create a new database for the branch you are using

2. Work on the normal database, and in case that you have to return to
   ``master`` or rollback the migration, do the steps manually.

.. _connect_to_the_database:

Connect to the Database
=======================

.. note::

    When using Postgres, the recommeded option is that the
    ``db-uri`` and ``state-db-uri`` reference the same database

There is more than one way that ``migratron`` can connect to the
PostgreSQL database:

- The PostgreSQL environment variables
- Specifing the ``db-uri`` argument

In both cases, you can read more information about this using the ``--help``
parameter. For example:

.. code-block:: console

    migratron migrate --help


For other Hive and PrestoDB, the ``db-uri`` argument is required because
there is no way to use the environment variables. For example, when using Hive,
you should use something like:

.. code-block:: console

    migratron migrate \
        --db-uri 'jdbc:hive2://localhost:10000/test' \
        --db-type hive \
        --state-db-uri postgres://foo:bar@localhost/test1'
