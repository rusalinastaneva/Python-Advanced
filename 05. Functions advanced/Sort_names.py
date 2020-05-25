names = input().split()
sorted_names = sorted(names, reverse=True)
print(*sorted_names)
# print(' '.join(sorted_names))