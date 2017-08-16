# -*- coding: utf-8 -*-
import click
from app import app
from config import PORT, HOST


def run_dev_server(host, port):
    click.echo("Starting dev server on {}:{}".format(host, port))
    app.run(host=host, port=port)
    click.echo("Started dev server on {}:{}".format(host, port))


@click.group()
def cli():
    pass


@cli.command(short_help="Run webserver")
@click.option("--host", default=HOST, help="Hostname (default: {})".format(HOST))
@click.option("--port", default=PORT, help="Port (default: {})".format(PORT))
def run(host, port):
    run_dev_server(host, port)


if __name__ == "__main__":
    cli()
