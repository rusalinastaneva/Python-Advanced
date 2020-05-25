def get_repeating_DNA(dna):
    dna_repetitions = []
    temp_results = []

    while len(dna) >= 10:
        current_result = dna[:10]
        if all([True if x in ["A", "G", "C", "T"] else False for x in current_result]):
            temp_results.append(current_result)
        dna = dna[1:]

    for x in temp_results:
        count = temp_results.count(x)
        if count > 1:
            dna_repetitions.append(x)
            temp_results.remove(x)
    return dna_repetitions

# def get_repeating_DNA(test):
#     list_result = []
#     i = 1
#     m = 10
#     while len(test) >= 10:
#         result_my = test[:10]
#         test = test[i:]
#         # if i == 10:
#         #     i = 1
#         if result_my in test:
#             i += 1
#             list_result.append(result_my)
#     return list_result



# test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
# result = get_repeating_DNA(test)
# print(result)
#
# test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
# result = get_repeating_DNA(test)
# print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
