def read_matrix():
    rows_count, cols_count = [int(x) for x in input().split()]
    matrix = [input().split() for _ in range(rows_count)]
    return matrix

def swap_indexes(matrix):
    cols_count = len(matrix[0])
    rows_count = len(matrix)
    line = input()

    while line != "END":
        args = line.split()
        command = args[0]
        if command == "swap" and len(args) == 5:
            row1 = int(args[1])
            col1 = int(args[2])
            row2 = int(args[3])
            col2 = int(args[4])
            if 0 <= row2 < rows_count and 0 <= col1 < cols_count and 0 <= row2 < rows_count and 0 <= col2 < cols_count:
                temp = matrix[row1][col1]
                matrix[row1][col1] = matrix[row2][col2]
                matrix[row2][col2] = temp
                [print(' '.join(map(str, row))) for row in matrix]
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
        line = input()

matrix = read_matrix()
swap_indexes(matrix)