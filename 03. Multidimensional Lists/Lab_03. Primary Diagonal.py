def read_matrix(line_delimiter):
    size = int(input())
    matrix = [list(map(int, input().split(line_delimiter))) for _ in range(size)]
    return matrix

def get_sum(matrix, row_func, col_func):
    n = len(matrix)
    the_sum = 0
    for x in range(n):
        row = row_func(x, n)
        col = col_func(x, n)
        the_sum += matrix[row][col]
    return the_sum

def get_sum_primary_diagonal(matrix):
    return get_sum(matrix,lambda x, n: x, lambda x, n: x)

# def get_sum_secondary_diagonal(matrix):
#     return get_sum(matrix, lambda x, n: x, lambda x, n: n - x - 1)

# def get_sum_secondary_diagonal(matrix):
#     n = len(matrix)
#     the_sum = 0
#     for x in range(n):
#         the_sum += matrix[x][n - x - 1]
#     return the_sum

matrix = read_matrix(" ")
print(get_sum_primary_diagonal(matrix))
