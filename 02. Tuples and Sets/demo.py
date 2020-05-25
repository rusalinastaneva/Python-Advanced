count = int(input())
students = {}

def average(grades_list):
    sum = 0
    for i in grades_list:
        sum += float(i)
    return sum / len(grades_list)

for _ in range(count):
    line = input().split()
    name = line[0]
    grade = float(line[1])
    if name not in students:
        students[name] = []
    students[name].append(f'{grade:.2f}')

[print(f'{key} - {" ".join(str(x) for x in value)} (avg: {average(value)})') for key, value in students.items()]