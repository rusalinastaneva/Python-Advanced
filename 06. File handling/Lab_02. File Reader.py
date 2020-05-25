file = open('files\\numbers.txt')

the_sum = 0
for line in file:
    the_sum += int(line)
print(the_sum)