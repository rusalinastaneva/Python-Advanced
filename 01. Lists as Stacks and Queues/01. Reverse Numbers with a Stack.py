nums = input().split()
result = []
for i in range(len(nums)):
    number = nums.pop()
    result.append(number)
print(' '.join(result))