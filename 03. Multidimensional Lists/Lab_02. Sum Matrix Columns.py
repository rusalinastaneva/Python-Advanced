def read_matrix(line_delimiter):
    rows, cols = list(map(int, input().split(", ")))
    matrix = [list(map(int, input().split(line_delimiter))) for _ in range(rows)]
    return matrix

def get_column_sums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    column_sum = [0] * cols
    for row in range(rows):
        for col in range(cols):
            column_sum[col] += matrix[row][col]
    return column_sum

matrix = read_matrix(" ")
[print(column_sum) for column_sum in get_column_sums(matrix)]