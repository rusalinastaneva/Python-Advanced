from _collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
match = 0

while females and males:
    current_female = females[0]
    current_male = males[-1]

    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.popleft()
    elif current_male == current_female:
        males.pop()
        females.popleft()
        match += 1
    elif current_female % 25 == 0:
        females.popleft()
        females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        males.pop()
    else:
        males.append(males.pop() - 2)
        females.popleft()


print(f'Matches: {match}')
if males:
    print(f'Males left: {", ".join(reversed([str(x) for x in males]))}')
else:
    print("Males left: none")

if females:
    print(f'Females left: {", ".join(map(str,females))}')
else:
    print("Females left: none")