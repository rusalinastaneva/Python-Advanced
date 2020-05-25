numbers_dictionary = {}

line = input()


class IsNotNumberStringError(Exception):
    """Raised when the value is a digit"""
    pass


while line != "Search":
    try:
        number_as_string = line
        if number_as_string.isdigit():
            raise IsNotNumberStringError("Input must be a string")
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    except IsNotNumberStringError as error:
        print(error)
    finally:
        line = input()

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()

print(numbers_dictionary)
