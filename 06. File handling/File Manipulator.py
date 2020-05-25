import os

command = input()

while command != "End":
    args = command.split("-")
    file_path = args[1]

    if args[0] == "Create":
        with open(file_path, 'w'):
            pass
    elif args[0] == "Add":
        content = args[2]
        with open(file_path, 'a') as file:
            file.write(f'{content}\n')
    elif args[0] == "Replace":
        old_string = args[2]
        new_string = args[3]
        try:
            with open(file_path, 'r') as file:
                line = file.read()
            new_line = line.replace(old_string, new_string)
            with open(file_path, 'w') as file:
                file.write(new_line)
        except FileNotFoundError:
            print("An error occurred")
    elif args[0] == "Delete":
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("An error occurred")
    command = input()
