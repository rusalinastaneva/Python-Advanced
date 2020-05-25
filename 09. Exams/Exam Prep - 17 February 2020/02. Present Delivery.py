dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
presents = int(input())
neighborhoods = int(input())
matrix = []
santa_position = []
nice_kids = 0
next_step = []
happy_kid = 0

for i in range(neighborhoods):
    line = input().split()
    if 'S' in line:
        santa_position = [i, line.index('S')]
    if 'V' in line:
        nice_kids += line.count('V')
    matrix.append(line)

while True:
    command = input()
    if command == "Christmas morning":
        break
    next_row = dirs[command][0] + santa_position[0]
    next_col = dirs[command][1] + santa_position[1]
    next_step = [next_row, next_col]

    if 0 <= next_col < len(matrix) and 0 <= next_row < len(matrix):
        if matrix[next_row][next_col] == 'X':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[next_row][next_col] = 'S'
            santa_position = next_step
        elif matrix[next_row][next_col] == 'V':
            happy_kid += 1
            presents -= 1
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[next_row][next_col] = 'S'
            santa_position = next_step

        elif matrix[next_row][next_col] == 'C':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[next_row][next_col] = 'S'
            santa_position = next_step
            dir = ('up', 'down', 'left', 'right')
            for el in dir:
                current_row = dirs[el][0] + santa_position[0]
                current_col = dirs[el][1] + santa_position[1]
                current_pos = [current_row, current_col]

                if 0 <= current_row < len(matrix) and 0 <= current_col < len(matrix):
                    if matrix[current_row][current_col] == 'V' or matrix[current_row][current_col] == "X" and presents:
                        presents -= 1
                        if matrix[current_row][current_col] == 'V':
                            happy_kid += 1
                        matrix[current_row][current_col] = '-'

        elif matrix[next_row][next_col] == '-':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[next_row][next_col] = 'S'
            santa_position = next_step

    if presents == 0:
        break

if presents == 0 and nice_kids - happy_kid != 0:
    print("Santa ran out of presents!")
[print(' '.join(row)) for row in matrix]

if happy_kid == nice_kids:
    print(f'Good job, Santa! {happy_kid} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids-happy_kid} nice kid/s.')