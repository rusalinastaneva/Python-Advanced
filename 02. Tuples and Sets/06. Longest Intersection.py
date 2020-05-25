n = int(input())
longest = []

for i in range(n):
    line = input().split("-")
    first_idx = list(map(int, line[0].split(',')))
    second_idx = list(map(int, line[1].split(',')))
    first_set = set(x for x in range(first_idx[0], first_idx[1] + 1))
    second_set = set(x for x in range(second_idx[0], second_idx[1] + 1))
    intercection = first_set.intersection(second_set)
    if len(intercection) > len(longest):
        longest = list(intercection)

print(f'Longest intersection is {longest} with length {len(longest)}')
