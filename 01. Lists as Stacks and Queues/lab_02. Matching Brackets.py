text = input()
indexes = []
for i in range(len(text)):
    if text[i] == "(":
        start_index = i
        indexes.append(start_index)
    if text[i] == ")":
        end_index = i
        start = indexes.pop()
        print(text[start:end_index + 1])