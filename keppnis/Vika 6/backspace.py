written = input()
to_list = list(written)

result = []

for i, char in enumerate(to_list):
    if char == '<':
        result.pop()
    else:
        result.append(char)



wanted = ''.join(result)
print(wanted)