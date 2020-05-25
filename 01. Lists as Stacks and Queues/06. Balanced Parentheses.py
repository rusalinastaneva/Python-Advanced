parenthesis = input()
stack = []
pairs = {
    '{':'}',
    '(':')',
    '[':']'
}
is_valid = True
for element in parenthesis:
    if element in '{([':
        stack.append(element)
    elif element in "})]":
        if stack:
            last_element = stack[-1]
            if pairs[last_element] == element:
                stack.pop()
            else:
                is_valid = False
                break
        else:
            is_valid = False
            break
if is_valid:
    print("YES")
else:
    print("NO")