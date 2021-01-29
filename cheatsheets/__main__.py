from .cheatsheets import cheatsheets
from .wizard import wizard
import click

@click.command()
@click.option('-w', is_flag=True, help='Launch Wizard')

def main(w):
    if w:
        wizard()
    else:
        cheatsheets()

if __name__ == '__main__':
    main()