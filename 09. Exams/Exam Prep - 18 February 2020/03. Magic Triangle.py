def get_magic_triangle(n):
    result = [[1], [1, 1]]

    for row in range(2, n):
        new_row = []
        for col in range(0, row + 1):
            if col - 1 < 0:
                new_row.append(1)
            elif col >= len(result[row-1]):
                new_row.append(1)
            else:
                upper_left = result[row - 1][col - 1]
                upper_right = result[row - 1][col]
                summed_value =  upper_left + upper_right
                new_row.append(summed_value)

        result.append(new_row)

    return result

print(get_magic_triangle(6))
