vowels = {'a', 'o', 'u', 'e', 'i'}
no_vowels = [x for x in input() if x.lower() not in vowels]
print(''.join(no_vowels))