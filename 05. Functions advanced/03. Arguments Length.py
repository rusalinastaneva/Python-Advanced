def args_length(*args):
    length = 0
    for _ in args:
        length += 1
    return length

print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))