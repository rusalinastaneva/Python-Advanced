from _collections import deque
line = input()
people = deque()

while line != "End":
    if line == "Paid":
        while people:
            print(people.popleft())
    else:
        people.append(line)

    line = input()

print(f"{len(people)} people remaining.")