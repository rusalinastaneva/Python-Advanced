from pyfiglet import figlet_format

def get_ascii_art(message):
    ascii_art = figlet_format(message)
    return ascii_art

msg = input("What would you like to print: ")
print(get_ascii_art(msg))