rows = int(input())
elements = set()
x = []
for i in range(rows):
    x = [x for x in input().split()]
    for el in x:
        elements.add(el)
[print(m) for m in elements]