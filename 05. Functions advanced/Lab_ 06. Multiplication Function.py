def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(5,2,3) == 25)