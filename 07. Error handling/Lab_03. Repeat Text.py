while True:
    try:
        text = input()
        n = int(input())
        print(n * text)
    except ValueError:
        print("Variable times must be an integer")
