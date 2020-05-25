def odd_or_even(command, *args):
    x = 0 if command == "Even" else 1
    filtered = map(lambda num: num % 2 == x, args)
    return sum(filtered) * len(args)

command = input()
nums = map(int, input().split())
print(odd_or_even(command, *nums))
