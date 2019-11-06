# -*- coding: utf-8 -*-

import os

#: the default path where the migrations are
current_path = os.path.dirname(__file__)

#: the name of the table with all the migrations information
MIGRATIONS_TABLENAME = "db_migrations"

#: the valid values that the user can use when running the different
#: commands in interactive mode
VALID_INPUT_VALUES = ("yes", "no")

MAIN_PARSER_DESCRIPTION = """
Used to setup or update the schema the Safiro DB Postgres Database.
It only works with Postgres database (from 9.2 forward).

It is important to take into account that once that the file is
executed it MUST not be updated because it won't be executed again.

To see more information, on the subcommand and parameters do:

    db-utils SUBCOMMAND --help

For example:

    db-utils initialize --help
"""

INITIALIZE_PARSER_DESCRIPTION = """
Used to initialize the database, and mark as already executed all
the migrations.

This is the first command that should be executed on the database
to be able to mark all the files as already executed and start
from there. But if you are starting with a new database created from
the `schema.sql` file, then you don't want to mark all the files as
marked. So you must use the `--just-base-schema` parameter to create
the migration table and mark the min number of files as processed

It is important to take into account that the executed date of
the different files is going to be today, but fell free to update them.

"""

MIGRATE_PARSER_DESCRIPTION = """
Identify the migrations that should be executed against the database.

This will work as follows:

- There is a table on the database that has all the already executed
  migrations

- There is a folder with all the existing migrations. It might have
  new ones or they already existed

- Once this command is executed, it will identify the migrations that
  should be executed. But this command won't execute the migrations.

- It will execute the migration

"""

CLEANUP_PARSER_DESCRIPTION = """
Deletes the flag from db_migrations that the file was already executed.
This isn't going to do a rollback of the migration, just delete
one row from the table.

This is used during development to take into account that if the
migration failed, you must re run the file but the database will
be left on an invalid state

NOTE: There is no way to identify if a migration is running of it
    failed, so make sure that when using this command the migration
    to delete is a failed one
"""
