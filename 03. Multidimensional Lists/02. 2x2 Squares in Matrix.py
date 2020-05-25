def read_matrix():
    rows_count, cols_count = [int(x) for x in input().split()]
    # matrix = [input().split() for _ in range(rows_count)]
    matrix = []
    for _ in range(rows_count):
        matrix.append(input().split())
    return matrix

def find_qty_squares(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    counter = 0
    for row in range(rows - 1):
        for col in range(cols - 1):
            current = matrix[row][col]
            up_right = matrix[row][col+1]
            down_right = matrix[row+1][col+1]
            down_left = matrix[row+1][col]
            if current == up_right == down_left == down_right:
                counter += 1
    return counter

matrix = read_matrix()
print(find_qty_squares(matrix))