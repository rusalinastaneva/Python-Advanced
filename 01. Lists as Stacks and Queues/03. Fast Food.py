from _collections import deque

available_food = int(input())
orders = deque(list(map(int, input().split(" "))))
print(max(orders))

while orders:
    current_order = orders.popleft()

    if available_food >= current_order:
        available_food -= current_order
    else:
        orders.appendleft(current_order)
        print(f'Orders left: {" ".join(str(x) for x in list(orders))}')
        break
if not orders:
    print("Orders complete")









