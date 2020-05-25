from math import log


def solve():
    number = int(input())
    base_str = input()
    result = 0
    if base_str == 'natural':
        result = log(number)
    else:
        result = log(number, int(base_str))
    return f'{result:.2f}'



print(solve())