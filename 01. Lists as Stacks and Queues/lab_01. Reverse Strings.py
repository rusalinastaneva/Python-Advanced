def solve(str):
    reversed = ''
    s = list(str)
    while s:
        reversed += s.pop()
    return reversed
text = input()
print(solve(text))