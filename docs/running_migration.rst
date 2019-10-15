==================
Running Migrations
==================

.. contents::
    :local:

``DB Utils`` is a very simple migration system:

Given a path where the migrations files are, it will check which are missing. For this,
it has a custom table on the database called ``db_migrations`` which has the path of
the executed files and whem they were executed.

First time
==========

If it is the first time you are running the migration against the database,
make sure to run the migration with the ``--just-base-schema`` to create the ``db_migrations``
table. Check :ref:`connect_to_the_database`

.. code-block:: console

    db-utils initialize --just-base-schema --migrations-path PATH_TO_MIGRATION_FILES


Once that the initial ``db-utils`` setup has been done you could just run the
migratinons as usuall

Running Missing Migrations
==========================

To update the database information, you must use:

.. code-block:: console

    db-utils migrate --migrations-path PATH_TO_MIGRATION_FILES

Run:

.. code-block:: console

    db-utils migrate --help

to get more information on the required parameters


Working With Branches
=====================

``DB-Utils`` doesn't take into account the different branches.
So there are two solutions:

1. Create a new database for the branch you are using

2. Work on the normal database, and in case that you have to return to
   ``master`` or rollback the migration, do the steps manually.

Connecting to the Database
==========================

There is more than one way that ``db-utils`` can use to connect to the
PostgreSQL database:

- The PostgreSQL environment variables
- Specifing the ``db-uri`` argument

In both cases, you can read more information about this using ``--help``
parameter. For example:

.. code-block:: console

    db-utils migrate --help


