from _collections import deque
duration_green = int(input())
window = int(input())
line = input()
cars = deque()
cars_counter = 0
crashed = False

while line != "END":
    if line == "green":
        if cars:
            current_car = cars.popleft()
            left_seconds = duration_green - len(current_car)

            while left_seconds > 0:
                cars_counter += 1
                if cars:
                    current_car = cars.popleft()
                    left_seconds -= len(current_car)
                else:
                    break
            if left_seconds == 0:
                cars_counter += 1
            if window >= abs(left_seconds):
                if left_seconds < 0:
                    cars_counter += 1
            else:
                index = window + left_seconds
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars.append(line)
    line = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")