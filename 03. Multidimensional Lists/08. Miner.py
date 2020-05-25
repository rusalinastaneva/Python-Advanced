def read_input():
    size = int(input())
    commands = input().split()
    matrix = [[x for x in input().split()] for _ in range(size)]
    return commands, matrix

commands, matrix = read_input()
rows_count = len(matrix)
cols_count = len(matrix[0])
miner_position = None
coals = 0
total_coals = 0
end = False

for i in range(rows_count):
    if "s" in matrix[i]:
        miner_position = i, matrix[i].index("s")
    total_coals += matrix[i].count("c")

for command in commands:
    start_row, start_col = miner_position
    next_step = None
    if command == "up":
        next_step = start_row-1, start_col
    elif command == "down":
        next_step = start_row+1, start_col
    elif command == "right":
        next_step = start_row, start_col+1
    elif command == "left":
        next_step = start_row, start_col - 1

    row, col = next_step
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if matrix[row][col] == "*":
            matrix[start_row][start_col] = "*"
            miner_position = next_step
        elif matrix[row][col] == "c":
            coals += 1
            matrix[start_row][start_col] = "*"
            miner_position = next_step
        elif matrix[row][col] == "e":
            print(f'Game over! {row, col}')
            end = True
            break

balance_coals = total_coals - coals

if not end:
    if balance_coals > 0:
        print(f'{balance_coals} coals left. {miner_position[0], miner_position[1]}')
    elif balance_coals == 0:
        print(f'You collected all coals! {miner_position[0], miner_position[1]}')
