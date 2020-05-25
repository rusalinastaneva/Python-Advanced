def read_matrix(line_delimiter):
    rows, cols = [int(x) for x in input().split(line_delimiter)]
    matrix = [list(map(int, input().split(line_delimiter))) for _ in range(rows)]
    return matrix


def find_best_sum_submatrix(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    best_sum = None
    best_start = None

    for row in range(rows_count - 1):
        for col in range(cols_count - 1):
            current_sum = matrix[row][col] + \
                          matrix[row][col + 1] + \
                          matrix[row + 1][col] + \
                          matrix[row + 1][col + 1]
            if best_sum:
                if best_sum < current_sum:
                    best_sum = current_sum
                    best_start = row, col
            else:
                best_sum = current_sum
                best_start = row, col

    row, col = best_start
    best_submatrix = [
        [matrix[row][col], matrix[row][col + 1]],
        [matrix[row + 1][col], matrix[row + 1][col + 1]]
    ]
    return best_sum, best_submatrix


matrix = read_matrix(", ")
best_sum, best_submatrix = find_best_sum_submatrix(matrix)
[print(' '.join(map(str, row))) for row in best_submatrix]
print(best_sum)
