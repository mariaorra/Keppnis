names = input()
letters = ''.join(name[0].upper() for name in names.split("-"))
print(letters)
