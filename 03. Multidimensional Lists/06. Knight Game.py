def read_matrix():
    size = int(input())
    matrix = [[x for x in input()] for _ in range(size)]
    return matrix

def get_damage(row, col, matrix):
    counter = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == "K":
            counter += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == "K":
            counter += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == "K":
            counter += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == "K":
            counter += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == "K":
            counter += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == "K":
            counter += 1
    return counter

matrix = read_matrix()
rows = len(matrix)
cols = len(matrix[0])
position = None
removed_knights = 0

while True:
    max_damage = 0
    for row in range(rows):
        for col in range(cols):
            current = matrix[row][col]
            if current == "K":
                damage = get_damage(row, col, matrix)
                if damage > max_damage:
                    max_damage = damage
                    position = row, col

    if max_damage == 0:
        break
    row, col = position[0], position[1]
    matrix[row][col] = "0"
    position = None
    removed_knights += 1

print(removed_knights)