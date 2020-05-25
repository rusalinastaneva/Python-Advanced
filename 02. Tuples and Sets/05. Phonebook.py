phonebook = {}
commands = input().split("-")

while commands[0] != 'search':
    name = commands[0]
    phone = commands[1]

    if name not in phonebook:
        phonebook[name] = phone
    else:
        phonebook[name] = phone
    commands = input().split("-")

name = input()

while name != 'stop':
    if name not in phonebook:
        print(f'Contact {name} does not exist.')
    else:
        print(f'{name} -> {phonebook[name]}')

    name = input()
