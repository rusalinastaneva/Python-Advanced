def func_executor(*args):
    results = []
    for arg in args:
        results.append(arg[0](*arg[1]))
    return results

# FOR TESTING
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))