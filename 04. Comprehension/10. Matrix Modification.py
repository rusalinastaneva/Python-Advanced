def read_matrix(delimiter):
    size = int(input())
    matrix = [list(map(int, input().split(delimiter))) for _ in range(size)]
    return matrix

def are_valid_coordinates(row, col, matrix):
    size = len(matrix)
    if 0 <= row < size and 0 <= col < size:
        return True

matrix = read_matrix(" ")

line = input()
while line != "END":
    command, row, col, num = line.split()
    if are_valid_coordinates(int(row), int(col), matrix):
        if command == "Add":
            matrix[int(row)][int(col)] += int(num)
        else:
            matrix[int(row)][int(col)] -= int(num)
    else:
        print("Invalid coordinates")
    line = input()

[print(' '.join(map(str, row))) for row in matrix]