text = input()
occurencies_of_chars = {}

for ch in text:
    if ch not in occurencies_of_chars:
        occurencies_of_chars[ch] = 0
    occurencies_of_chars[ch] += 1

for key, value in dict(sorted(occurencies_of_chars.items())).items():
    print(f'{key}: {value} time/s')
