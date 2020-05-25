def read_matrix(delimeter):
    size = int(input())
    matrix = [list(map(int, input().split(delimeter))) for _ in range(size)]
    return matrix

def get_sum(matrix, row_def, col_def):
    size = len(matrix)
    the_sum = 0
    for x in range(size):
        row = row_def(x, size)
        col = col_def(x, size)
        the_sum += matrix[row][col]
    return the_sum

def sum_primary_diagonal(matrix):
    return get_sum(matrix, lambda x, n: x, lambda x, n: x)
def sum_secondary_diagonal(matrix):
    return get_sum(matrix, lambda x, n: x, lambda x, n: n - x - 1)

matrix = read_matrix(" ")
difference = abs(sum_primary_diagonal(matrix) - sum_secondary_diagonal(matrix))
print(difference)