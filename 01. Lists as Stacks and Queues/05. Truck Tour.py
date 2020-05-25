n = int(input())
start_idx = 0
fuel = 0

for i in range(n):
    petrol, distance = [int(x) for x in input().split()]
    fuel += petrol

    if fuel >= distance:
        fuel -= distance
    else:
        start_idx = i + 1
        fuel = 0

print(start_idx)

