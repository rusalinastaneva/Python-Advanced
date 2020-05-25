(rows_count, columns_count) = map(int, input().split())
matrix = []
new_matrix = []
player_position = []
player_wins = False

for i in range(rows_count):
    row = [x for x in input()]
    if "P" in row:
        player_position = [i, row.index("P")]
        row[row.index("P")] = "."
    row2 = row.copy()
    matrix.append(row)
    new_matrix.append(row2)

commands = list(input())

for command in commands:
    next_player_position = []
    if command == "U":
        next_player_position = [player_position[0] - 1, player_position[1]]
    elif command == "D":
        next_player_position = [player_position[0] + 1, player_position[1]]
    elif command == "L":
        next_player_position = [player_position[0], player_position[1] - 1]
    elif command == "R":
        next_player_position = [player_position[0], player_position[1] + 1]

    for r in range(rows_count):
        for ch in range(columns_count):
            if matrix[r][ch] == "B":
                if r - 1 >= 0:
                    new_matrix[r - 1][ch] = "B"
                if ch - 1 >= 0:
                    new_matrix[r][ch - 1] = "B"
                if ch + 1 < columns_count:
                    new_matrix[r][ch + 1] = "B"
                if r + 1 < rows_count:
                    new_matrix[r + 1][ch] = "B"
    matrix = [x.copy() for x in new_matrix]

    if 0 <= next_player_position[0] <= rows_count - 1 and 0 <= next_player_position[1] <= columns_count - 1:
        player_position = next_player_position
        if matrix[player_position[0]][player_position[1]] == "B":
            break
    else:
        player_wins = True
        break

[print("".join(x)) for x in matrix]
if player_wins:
    print(f"won: {player_position[0]} {player_position[1]}")
else:
    print(f"dead: {player_position[0]} {player_position[1]}")