def kwargs_length(**kwargs):
    length = 0
    for key in kwargs:
        length += 1
    return length


# for testing
dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
