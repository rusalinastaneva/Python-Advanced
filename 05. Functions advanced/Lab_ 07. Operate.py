def operate(operator, *args):
    result = 0
    if operator == '*' or operator == '/':
        result = 1
    for num in args:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            result /= num
    return result

# import operator
# def operate(sign, *args):
#     operations = {
#         "+": operator.add,
#         "-": operator.sub,
#         "*": operator.mul,
#         "/": operator.truediv,
#     }
#     result = args[0]
#     for x in args[1:]:
#         result = operations[sign](result, x)
#     return result
#
# print(operate("-", 10, 2, 1.1))
# print(operate("+", 0))
# print(operate("*", 3, 2, 10, 8))
# print(operate("/", 10, 2, 5))
