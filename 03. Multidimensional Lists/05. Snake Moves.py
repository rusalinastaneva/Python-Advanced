from _collections import deque
rows_count, cols_count = [int(x) for x in input().split()]
matrix = [[""] * cols_count for _ in range(rows_count)]
text = deque(x for x in input())

for row in range(rows_count):
    for col in range(cols_count):
        if text:
            current_element = text.popleft()
            text.append(current_element)
            if row % 2 == 0:
                matrix[row][col] = current_element
            else:
                matrix[row][cols_count - col - 1] = current_element
[print(''.join(row)) for row in matrix]

