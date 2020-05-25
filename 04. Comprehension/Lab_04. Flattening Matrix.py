rows_count = int(input())
matrix = [map(int, input().split(", ")) for _ in range(rows_count)]
flattened = [x for sublist in matrix for x in sublist]

print(flattened)