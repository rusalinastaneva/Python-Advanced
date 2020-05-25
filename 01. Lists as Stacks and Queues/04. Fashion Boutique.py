box = list(map(int, input().split()))
capacity = int(input())
racks = 0
sum = 0

while box:
    current = box[-1]
    if capacity >= sum + current:
        sum += box.pop()
    else:
        sum = 0
        racks += 1

if sum > 0:
    racks += 1
print(racks)


