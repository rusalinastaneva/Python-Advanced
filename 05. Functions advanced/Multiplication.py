n = int(input())
numbers = map(int, input().split())
result = map(lambda x: x * n, numbers)
print(*result)