from _collections import deque
def solve():
    liters = int(input())
    person = input()
    people = deque()
    person_liters = 0

    while person != "Start":
        people.append(person)
        person = input()

    while people:
        command = input()
        if command.startswith('refill'):
            liters += int(command.split()[1])
            continue
        person = people.popleft()
        person_liters = int(command)
        if person_liters <= liters:
            print(f'{person} got water')
            liters -= person_liters
        else:
            print(f'{person} must wait')
    print(f'{liters} liters left')

solve()
