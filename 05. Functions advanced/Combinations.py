def combinations(start, end, k, comb=[]):
    if len(comb) == k:
        print(comb)
        return
    for x in range(start, end + 1):
        comb.append(x)
        combinations(x + 1, end, k, comb)
        comb.pop()

combinations(1, 4, 2)