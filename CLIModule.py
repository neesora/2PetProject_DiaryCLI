from diaryMain import Diary
import click
from sqlite_utils.db import NotFoundError

@click.group()
def cli():
    """my cli"""
    pass
#create the top-level parser and create class-insance
diary = Diary()
@cli.command("append")
@click.option("--entry", prompt="Input some text", help="The diary entry")
@click.option("--mood", prompt="Input the mood", help="The mood of the entry")
def append(entry, mood):
    """Append a new diary entry"""
    word = diary.append(entry, mood)
    if word == "Error":
        click.echo(f"Record already exists with that primary key")
    else:
        diary.append(entry, mood)
        click.echo(f"Entry appended successfully!")

@cli.command("search")
@click.option("--search", prompt="Input day search", help="Date for search")
def search(search):
    """Search entry"""
    row = diary.search(search)
    click.echo(f"Founded entry: {row}")

@cli.command("edit")
@click.option("--edit", prompt="Input ID for edit", help="Date for search")
@click.option("--entry", prompt="Input new text", help="The edit entry")
@click.option("--mood", prompt="Input new mood", help="The edit mood of the entry")
def change(search, entry, mood):
    """Edit entry"""
    word = diary.change(search, entry, mood)
    if word == "Error":
        click.echo(f"Row isn't founded")
    else:
        diary.change(search, entry, mood)
        click.echo(f"Row was succesful edited")

@cli.command("del")
@click.option("--remove", prompt="Input ID for del", help="Row ID for deletion")
def remove(remove):
    """Remove entry"""
    word = diary.remove(remove)
    if word == "Error":
        click.echo(f"Row isn't founded")
    else:
        diary.remove(remove)
        click.echo(f"Row was succesful removed")

if __name__ == '__main__':
    cli()