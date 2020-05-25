def find_count(numbers, target, expression= ''):
    if not numbers:
        print(expression)
        if target == 0:
            return 1
        else:
            return 0
    result = 0

    result += find_count(numbers[1:], target - numbers[0], expression + f'+{numbers[0]}')
    result += find_count(numbers[1:], target + numbers[0], expression + f'-{numbers[0]}')
    return result

print(find_count([1, 2, 1], 4))