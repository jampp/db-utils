========================
Creating a new Migration
========================

.. warning::

    Never edit an already executed migration. Just create a new one

First of all, there are 2 types of migrations:

.. glossary::

    PRE
        These migrations are the ones that are backwards compatible. For example,
        add a column or table, or solve an issue on a view.

    POST
        These migrations are used to cleanup the database once that all the
        servers code has been updated. These migrations are the ones that drop
        a column or table.

This is to take into account that all the servers can't be updated at the same
time (which would cause some downtime). For example, if we want to rename a
column there should be a :term:`PRE` and a :term:`POST` migration:

- The :term:`PRE` should create the new column and populate the value from the
  existing column

- The :term:`POST` should delete the old column



The migration filename should follow the following template:
``YYYYMMDD_index_(pre or post)_(small description).sql``. For example:
``20160801_0_pre_add_foobar_column.sql``. This isn't optional because
the migration system will fail if the migration doesn't follow that
format. The index is used to take into account that the same date can
have more than one migration so the index identifies the order on which
those file should be executed

