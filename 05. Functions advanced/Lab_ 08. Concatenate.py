def concatenate(*args):
    result = ''
    for element in args:
        result += element
    return result

print(concatenate("Soft", "Uni", "Is", "Great", "!"))