from _collections import deque
from math import floor

line = deque(input().split(" "))
numbers = deque()
result = 0

while line:
    if line[0].lstrip('-').isdigit() or line[0].isdigit():
        current_num = line.popleft()
        numbers.append(int(current_num))
    elif line[0] in "-+*/":
        operator = line.popleft()
        while numbers:
            if len(numbers) == 1:
                break
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if operator == "+":
                result = first_num + second_num
            elif operator == "-":
                result = first_num - second_num
            elif operator == "*":
                result = first_num * second_num
            elif operator == "/":
                result = first_num / second_num
                result = floor(result)
            numbers.appendleft(result)

print(f'{result}')
