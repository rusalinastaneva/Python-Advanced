def permutations(index, values):
    if index == len(values):
        print(values)
        return

    for i in range(index, len(values)):
        values[index], values[i] = values[i], values[index]
        permutations(index + 1, values)
        values[index], values[i] = values[i], values[index]

values = list(range(1,4))
permutations(0, values)