numbers = map(int, input().split())
negative_nums = list(filter(lambda x: x < 0, numbers))
abs_sum = abs(sum(negative_nums))
print(abs_sum)