def read_matrix():
    rows_count, cols_count = [int(x) for x in input().split()]
    matrix = [list(map(int, input().split())) for _ in range(rows_count)]
    return matrix

def calculate_max_sum_square(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    best_sum = None
    start_idx = None

    for row in range(rows_count-2):
        for col in range(cols_count-2):
            current_sum = matrix[row][col] + \
                  matrix[row][col + 1] + \
                  matrix[row][col + 2] + \
                  matrix[row + 1][col] + \
                  matrix[row + 1][col + 1] + \
                  matrix[row + 1][col + 2] + \
                  matrix[row + 2][col] + \
                  matrix[row + 2][col + 1] + \
                  matrix[row + 2][col + 2]

            if best_sum:
                if current_sum > best_sum:
                    best_sum = current_sum
                    start_idx = row, col
            else:
                best_sum = current_sum
                start_idx = row, col

    row, col = start_idx
    best__submatrix = [
        [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
        [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
        [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
    ]
    return best_sum, best__submatrix

matrix = read_matrix()
best_sum, best__submatrix = calculate_max_sum_square(matrix)
print(f'Sum = {best_sum}')
[print(' '.join(map(str, row))) for row in best__submatrix]