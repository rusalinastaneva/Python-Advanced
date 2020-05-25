# input_line = input().split(' ')
# numbers_as_str = filter(lambda x: x.isdigit(), input_line)
# numbers = filter(lambda x: x > len(input_line), map(int, numbers_as_str))
# print(sorted(numbers))

input_line = input().split(' ')
# numbers = [int(x) for x in input_line if x.isdigit() and int(x) > len(input_line)]
numbers = [int(x) for x in input_line if x.isdigit()]
numbers = filter(lambda x: x > len(input_line), numbers)
print(sorted(numbers))
