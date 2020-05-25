def palindrome(text, idx):
    second_idx = len(text) - idx - 1
    if idx == len(text) // 2:
        return f'{text} is a palindrome'
    if text[idx] == text[second_idx]:
        return palindrome(text, idx + 1)
    else:
        return f'{text} is not a palindrome'
print(palindrome("abcba", 0))
print(palindrome("peter", 0))