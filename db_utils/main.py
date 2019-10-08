# -*- coding: utf-8 -*-

from db_utils.parsers import create_command_line_parser
from db_utils.command.initialize import InitializeCommand
from db_utils.command.run_migration import RunMigrationCommand
from db_utils.command.cleanup import CleanupCommand


def main(args=None):
    """ Entrypoint when you run `db-utils` on the console
    """
    parser = create_command_line_parser()
    parsed_args = parser.parse_args(args=args)
    subparser_name = parsed_args.subparser_name
    subparser_class = dict(
        initialize=InitializeCommand,
        migrate=RunMigrationCommand,
        cleanup=CleanupCommand
    )
    klass = subparser_class[subparser_name]
    kwargs = vars(parsed_args)
    kwargs.pop('subparser_name')
    command = klass(**kwargs)
    command.run()


if __name__ == '__main__':
    main()
