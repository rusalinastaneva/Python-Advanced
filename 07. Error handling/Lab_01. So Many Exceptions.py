numbers_list = list(map(int, input().split(", ")))
result = 1
# 1, 4, 5 : 20
for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number > 5 and number <= 10:
        result /= number

print(int(result))
