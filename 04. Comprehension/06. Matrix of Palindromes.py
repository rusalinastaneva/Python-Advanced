rows_count, cols_count = [int(x) for x in input().split()]
matrix = [[""] * cols_count for _ in range(rows_count)]

for row in range(rows_count):
    for col in range(cols_count):
        first_and_last_char = chr(ord("a") + row)
        mid_char = chr(ord("a") + row + col)
        matrix[row][col] = first_and_last_char + mid_char + first_and_last_char
[print(' '.join(row)) for row in matrix]