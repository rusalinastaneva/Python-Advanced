def is_valid(number):
    min_num = 2
    max_num = 10
    # for y in range(min_num, max_num + 1):
    #     if number % y == 0:
    #         return True
    # return False
    result = [y for y in range(min_num, max_num + 1) if number % y == 0]
    return result

start = int(input())
end = int(input())
# filtered = [num for num in range(start, end + 1) if any([num % y == 0 for y in range(2, 11)])]
filtered = [num for num in range(start, end + 1) if is_valid(num)]
print(filtered)