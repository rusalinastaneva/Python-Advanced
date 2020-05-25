def read_input():
    size = int(input())
    return (
        [input() for _ in range(size)],
        input()
    )


def get_position_symbol(matrix, symbol):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if symbol == matrix[row][col]:
                return row, col
    return None


matrix, symbol = read_input()
result = get_position_symbol(matrix, symbol)

if result:
    row, col = get_position_symbol(matrix, symbol)
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')
