size = int(input())
matrix = []
plane_pos = None
targets = 0
killed_targets = 0
dirs = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'p' in line:
        plane_pos = row, line.index('p')
    if 't' in line:
        targets += line.count('t')

n = int(input())
for _ in range(n):
    line = input().split()
    command = line[0]
    direction = line[1]
    steps = int(line[2])
    if direction == 'down' or direction =='up':
        next_row = dirs[direction][0] * steps + plane_pos[0]
        next_col = dirs[direction][1] + plane_pos[1]
    else:
        next_row = dirs[direction][0] + plane_pos[0]
        next_col = dirs[direction][1] * steps + plane_pos[1]
    next_step = [next_row, next_col]

    if 0 <= next_col < len(matrix) and 0 <= next_row < len(matrix):
        if command == 'shoot':
            if matrix[next_row][next_col] == 't':
                killed_targets += 1

            matrix[next_row][next_col] = 'x'
        elif command == 'move':
            if matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'p'
                matrix[plane_pos[0]][plane_pos[1]] = '.'
                plane_pos = next_step

        if targets == killed_targets:
            print(f"Mission accomplished! All {targets} targets destroyed.")
            break


if targets != killed_targets:
    print(f'Mission failed! {targets - killed_targets} targets left.')

[print(' '.join(row)) for row in matrix]