#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function

import click
from impala.dbapi import connect
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from .lexer import ImpalaLexer
from cli_helpers.tabular_output import TabularOutputFormatter

click.disable_unicode_literals_warning = True


class ImpalaCli:

    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.conn = None
        self.connect()

    def connect(self):
        self.conn = connect(host=self.host, port=self.port,
                            database=self.database)

    def run_cli(self):
        cursor = self.conn.cursor()

        formatter = TabularOutputFormatter(format_name='psql')
        history = InMemoryHistory()

        def get_prompt_message():
            layout = '{host}/{database}> '
            cursor.execute('SELECT current_database()')
            result = cursor.fetchone()

            return layout.format(host=self.host, database=result[0])

        while True:
            try:
                statement = prompt(get_prompt_message(), lexer=ImpalaLexer, history=history)
            except EOFError:
                click.echo('GoodBye!')
                self.conn.close()
                break

            try:
                cursor.execute(statement)
            except Exception as e:
                print(str(e))
                continue

            if cursor.description is not None:
                data = cursor.fetchall()
                header = (item[0] for item in cursor.description)
                output = formatter.format_output(data=data, headers=header)

                for line in output:
                    click.echo(line)


@click.command()
@click.argument('database', required=False)
@click.option('-h', '--host', required=True, help='host to connect')
@click.option('-p', '--port', default=21050, help='port of host')
def cli(host, database, port):
    impcli = ImpalaCli(host=host, port=port,
                       database=database)
    impcli.run_cli()


if __name__ == '__main__':
    cli()
