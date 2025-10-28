"""Console script for string_calculator_kata."""

import typer
from rich.console import Console

from string_calculator_kata import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for string_calculator_kata."""
    console.print(
        "Replace this message by putting your code into "
        "string_calculator_kata.cli.main"
    )
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
