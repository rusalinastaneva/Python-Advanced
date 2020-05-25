line = input().split("|")
matrix = [x.split() for x in line]
new_matrix = [matrix.pop() for sublist in matrix[::-1] if matrix]
print(' '.join([num for sublist in new_matrix for num in sublist]))

# import re
#
# matrix = [x.split() for x in re.split('\|', input())]
# new_matrix = [matrix.pop() for sublist in matrix[::-1] if matrix]
# print(' '.join([num for sublist in new_matrix for num in sublist]))