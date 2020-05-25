numbers = list(map(int, input().split()))
n, s, x = numbers

elements = [int(x) for x in input().split()]

[elements.pop() for _ in range(s)]

if elements != 0:
    if x in elements:
        print('True')
    else:
        print(min(elements))
else:
    print(0)