from drawings.lines import print_line


def print_triangle(n):
    [print_line(row) for row in range(n)]
    [print_line(row) for row in range(n - 2, -1, -1)]
