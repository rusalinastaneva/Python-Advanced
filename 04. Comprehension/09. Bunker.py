categories = input().split(", ")
rows = int(input())
bunker = {category: {} for category in categories}

for i in range(rows):
    args = input().split(" - ")
    category = args[0]
    item = args[1]
    items_args = args[2].split(";")
    qty = int(items_args[0].split(":")[1])
    quality = int(items_args[1].split(":")[1])

    if category in bunker:
        bunker[category][item] = [qty, quality]

count_items = sum([inner_map[elem][0] for inner_map in bunker.values() for elem in inner_map])
print(f'Count of items: {count_items}')

sum_quality = sum([inner_map[elem][1] for inner_map in bunker.values() for elem in inner_map])
print(f'Average quality: {sum_quality / len(categories):.2f}')
[print(f'{key} -> {", ".join(inner_map.keys())}') for key, inner_map in bunker.items()]
