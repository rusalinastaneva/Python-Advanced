n = int(input())
nums = []
for i in range(n):
    elements = list(map(int, input().split()))

    if elements[0] == 1:
        nums.append(elements[1])
    if nums:
        if elements[0] == 2:
            nums.pop()
        if elements[0] == 3:
            print(max(nums))
        if elements[0] == 4:
            print(min(nums))

print(', '.join([str(num) for num in nums[::-1]]))