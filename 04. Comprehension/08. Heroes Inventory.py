keys = input().split(", ")
inventory = {hero: {} for hero in keys}
command = input()

while command != "End":
    name, item, cost = command.split("-")

    if name in inventory:
        if item not in inventory[name]:
            inventory[name][item] = int(cost)
    command = input()

[print(f'{k} -> Items: {len(inventory[k])}, Cost: {sum(v_dict.values())}') for k, v_dict in inventory.items()]
