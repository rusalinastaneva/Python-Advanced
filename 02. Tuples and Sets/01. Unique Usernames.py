n = int(input())
names = {input() for name in range(n)}
[print(name) for name in names]