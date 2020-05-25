nums = map(int, input().split(' '))
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)