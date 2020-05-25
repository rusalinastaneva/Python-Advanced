names = input().split()
filtered = filter(lambda x: x.istitle(), names)
sum_length = sum(map(lambda x: len(x), filtered))
print(sum_length)