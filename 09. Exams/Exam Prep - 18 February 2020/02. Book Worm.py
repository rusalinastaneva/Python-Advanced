intial_str = input()
rows = int(input())
player_position = []
matrix = []

for i in range(rows):
    row = list(input())
    if "P" in row:
        player_position = [i, row.index('P')]
    matrix.append(row)

moves = int(input())
for i in range(moves):
    direction = input()
    next_step = None
    start_row, start_col = player_position[0], player_position[1]

    if direction == 'up':
        next_step = start_row - 1, start_col
    elif direction == 'down':
        next_step = start_row + 1, start_col
    elif direction == 'left':
        next_step = start_row, start_col - 1
    elif direction == 'right':
        next_step = start_row, start_col + 1

    row, col = next_step
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col].isalpha():
            intial_str += matrix[row][col]
            matrix[player_position[0]][player_position[1]] = '-'
            player_position = next_step
            matrix[row][col] = 'P'
        elif matrix[row][col] == '-':
            matrix[player_position[0]][player_position[1]] = '-'
            player_position = next_step
            matrix[row][col] = 'P'
    else:
        if intial_str:
            intial_str = intial_str[:-1]


print(intial_str)
[print(''.join(x)) for x in matrix]