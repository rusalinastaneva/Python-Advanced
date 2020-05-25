from _collections import deque

materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}
while materials and magic_values:
    current_material = materials.pop()
    current_magic = magic_values.popleft()
    total_magic = current_material * current_magic

    if total_magic in presents:
        present = presents[total_magic]
        crafted[present] += 1
    else:
        if total_magic < 0:
            the_sum = current_magic + current_material
            materials.append(the_sum)
        elif total_magic > 0:
            materials.append(current_material + 15)
        else:
            if current_material:
                materials.append(current_material)
            if current_magic:
                magic_values.appendleft(current_magic)

if (crafted['Bicycle'] and crafted['Teddy bear'] or crafted['Doll'] and crafted['Wooden train']) > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join(map(str, reversed(materials)))}')
if magic_values:
    print(f'Magic left: {", ".join(map(str, magic_values))}')

for key, value in sorted(crafted.items()):
    if value:
        print(f'{key}: {value}')