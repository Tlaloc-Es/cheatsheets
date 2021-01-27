from simple_term_menu import TerminalMenu
from pygments import formatters, highlight, lexers
from pygments.util import ClassNotFound
import json
import os
import re
from . import CHEAT_DIRECTORY


def preview_cheat(cheat):
    filepath = CHEAT_DIRECTORY+cheat
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def list_cheats():
    return [file for file in os.listdir(CHEAT_DIRECTORY) if os.path.isfile(os.path.join(CHEAT_DIRECTORY, file))]


def execute_cheat(cheat):

    with open(CHEAT_DIRECTORY+cheat) as f:
        data = json.load(f)
    
    command = data['command']
    try:
        arg = re.search('<(.+?)>', command).group(1)
        while arg:
            arg_val = input(f'Insert value for arg: {arg}\n')
            command = command.replace(f'<{arg}>', arg_val, 1)
            arg = re.search('<(.+?)>', command).group(1)
            print(command+'\n')
    except Exception:
        pass

    os.system(command)


def main():
    cheats = list_cheats()

    if len(cheats) > 0:
        terminal_menu = TerminalMenu(cheats, preview_command=preview_cheat, preview_size=0.75)
        menu_entry_index = terminal_menu.show()
        execute_cheat(cheats[menu_entry_index])
    else:
        print("You don't have any cheat")

if __name__ == "__main__":
    main()