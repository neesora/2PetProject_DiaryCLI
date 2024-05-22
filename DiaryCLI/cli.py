from DiaryCLI.diaryMain import Diary
import click

diary = Diary()
@click.group()
def cli():
    """my cli"""
    pass

#create the top-level parser and create class-insance
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

@cli.command("change")
@click.option("-t", "--today", prompt="Input date for search", help="Date for search")
def picker(today):
    """Edit entry"""
    check = diary.change(today, None)
    if check:
        click.echo("Entry not found")
    else:
        click.echo(f"Row was succesful edited")

if __name__ == '__main__':
    cli()
