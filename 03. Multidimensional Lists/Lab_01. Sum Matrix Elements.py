def sum_matrix_elements(matrix):
    the_sum = 0
    rows = len(matrix)

    for row_idx in range(rows):
        row = matrix[row_idx]
        the_sum += sum(row)
    return the_sum

def read_matrix():
    rows, cols = list(map(int, input().split(", ")))
    matrix = []
    for _ in range(rows):
        line = list(map(int, input().split(", ")))
        matrix.append(line)
    return matrix

matrix = read_matrix()
print(sum_matrix_elements(matrix))
print(matrix)
