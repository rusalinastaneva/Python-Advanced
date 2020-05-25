from _collections import deque

def solve(people, n):
    people = deque(people)
    i = 0
    # n = 10 000
    # len = 5
    while len(people) > 1:
        i += 1
        kid = people.popleft()
        if n == i:
            i = 0
            print(f'Removed {kid}')
        else:
            people.append(kid)
    print(f'Last is {people.popleft()}')

solve(input().split(), int(input()))