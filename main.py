#! /usr/bin/env python3
"""
Honing my CLI creation skills
"""
from pathlib import Path
import logging
import click

logging.basicConfig(
    format="{asctime}--{levelname}--{name}: {message}",
    style="{",
    level=logging.INFO,
    datefmt="%Y/%m/%d %H:%M:%S",
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@click.command()
@click.version_option(version="0.0.1", prog_name="ls")
@click.argument(
    "path",
    type=click.Path(exists=True, dir_okay=True, path_type=Path),
    default= Path.cwd(),
)
def ls(path):
    """ls command"""
    print(f"The default path is {path}")
    if not path:
        path = Path.cwd()

    for file in path.iterdir():
        click.secho(f"{file.name}", fg="green")

if __name__=="__main__":
    ls()