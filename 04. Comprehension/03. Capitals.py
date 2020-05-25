countries = input().split(", ")
capitals = input().split(", ")
[print(f'{x} -> {y}') for x, y in zip(countries, capitals)]
