def binary_search(values, target):
    if not values:
        return False
    if len(values) == 1:
        return values[0] == target

    mid = len(values) // 2
    if values[mid] == target:
        return True
    elif values[mid] < target:
        return binary_search(values[mid:], target)
    else:
        return binary_search(values[:mid], target)