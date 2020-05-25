def negative_vs_positive(*args):
    sum_negative = sum([num for num in args if num < 0])
    sum_positive = sum([num for num in args if num > 0])
    print(sum_negative)
    print(sum_positive)
    result = 'The negatives are stronger than the positives' if abs(sum_negative) > sum_positive \
        else 'The positives are stronger than the negatives'
    return result

nums = [int(x) for x in input().split()]
print(negative_vs_positive(*nums))