#!/usr/bin/env python

import click

from .commands import initdb, revision, up
from .logic import Context, ConsoleUserInterface


@click.group(help="CLI tool to manage migrations")
def cli() -> None:
    pass


@click.argument('config_path', default="/Users/jj/REPOS/wave/migrator/test/migrator.yml")
@click.argument('database_url', default="postgresql://migrator:rotargim@localhost:5543")
@click.command('init')
def init(config_path: str, database_url: str) -> None:
    ctx = Context(config_path=config_path, database_url=database_url, ui=ConsoleUserInterface())
    initdb.initdb(ctx)


@click.argument('config_path', default="/Users/jj/REPOS/wave/migrator/migrator.yml")
@click.argument('database_url', default="postgresql://migrator:rotargim@localhost:5543")
@click.argument('message')
@click.command('revision')
def revision_command(config_path: str, database_url: str, message: str) -> None:
    ctx = Context(config_path=config_path, database_url=database_url, ui=ConsoleUserInterface())
    revision.revision(ctx, message)


@click.argument('config_path', default="/Users/jj/REPOS/wave/migrator/migrator.yml")
@click.argument('database_url', default="postgresql://migrator:rotargim@localhost:5543")
@click.command('up')
def up_command(config_path: str, database_url: str) -> None:
    ctx = Context(config_path=config_path, database_url=database_url, ui=ConsoleUserInterface())
    up.up(ctx)


cli.add_command(init)
cli.add_command(revision_command)
cli.add_command(up_command)

if __name__ == '__main__':
    cli()
