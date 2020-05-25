n, m = [int(x) for x in input().split()]
first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}
# common_elements = first_set.intersection(second_set)
[print(num) for num in first_set & second_set]