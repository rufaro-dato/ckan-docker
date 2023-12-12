import click


@click.group(short_help="rufaro CLI.")
def rufaro():
    """rufaro CLI.
    """
    pass


@rufaro.command()
@click.argument("name", default="rufaro")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [rufaro]
