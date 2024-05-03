from diaryMain import Diary
import click

@click.group()
def cli():
    """my cli"""
    pass
#create the top-level parser and create class-insance
diary = Diary()
@cli.command("append")
@click.option("-e", "--entry", prompt="Input some text", help="The diary entry")
@click.option("-m", "--mood", prompt="Input the mood", help="The mood of the entry")
def append(entry, mood):
    """Append a new diary entry"""
    word = 0
    if word == "Error":
        click.echo(f"Record already exists with that primary key")
    else:
        diary.append(entry, mood)
        click.echo(f"Entry appended successfully!")

@cli.command("search")
@click.option("-t", "--today", prompt="Input day search", help="Date for search")
def search(today):
    """Search entry"""
    row = diary.search(today, None, None)
    if row:
        click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
    else:
        click.echo("Entry not found")

@cli.command("edit")
@click.option("-t", "--today", prompt="Input date for search", help="Date for search")
def search(today):
    """Edit entry"""
    row = diary.search(today, None, None)
    do = diary
    if row:
        click.echo(f"Founded entry: \n Date: {row[1]} Entry: {row[2]} Mood: {row[3]}")
    else:
        diary.change(today, 0, 0, row)
        click.option("-e", "--entry", prompt="Input new text", help="The edit entry")
        click.option("-m", "--mood", prompt="Input new mood", help="The edit mood of the entry")
        click.echo(f"Row was succesful edited")

@cli.command("del")
@click.option("-r", "--remove", prompt="Input ID for del", help="Row ID for deletion")
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