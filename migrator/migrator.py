#!/usr/bin/env python

import click

from .commands import initdb, revision, up


@click.group(help="CLI tool to manage migrations")
def cli() -> None:
    pass


cli.add_command(initdb.initdb)
cli.add_command(up.up)
# cli.add_command(revision.revision)

if __name__ == '__main__':
    cli()
