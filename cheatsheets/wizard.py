import json
from pathlib import Path
from os.path import isfile
from . import CHEAT_DIRECTORY

def wizard():
    try:
        cheatsheet = {}
        cheatsheet_file = ''
        
        input_ok = False

        while not input_ok:
            cheatsheet['name'] = input("Insert name of the new Cheatsheet: ")
            filename = ''.join(filter(str.isalpha, cheatsheet['name'].capitalize()))
            cheatsheet_file = f'{CHEAT_DIRECTORY}{filename}.json'

            if isfile(cheatsheet_file):
                print('Cheatsheet already exists')
            elif cheatsheet['name'] == '':
                print('Insert a valid name')
            else:
                input_ok = True
        
        while not cheatsheet.get('command'):
            cheatsheet['command'] = input("Insert command, you can set arguments betwen <> like <directory>: ")

            if cheatsheet['command'] == '':
                print('Insert a valid command')

        while not cheatsheet.get('description'):
            cheatsheet['description'] = input("Insert a short description of your cheatsheet: ")

        with open(cheatsheet_file, 'w', encoding='utf-8') as f:
            json.dump(cheatsheet, f, ensure_ascii=False, indent=4)

        print(f'Cheatsheet created in: {cheatsheet_file}')
        print(f'You can edit with "nano {cheatsheet_file}"')

    except:
        pass

if __name__ == "__main__":
    main()