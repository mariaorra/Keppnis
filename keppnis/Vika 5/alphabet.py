s = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

table = [[0 for _ in range(len(alphabet)+1)] for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    for j in range(1, len(alphabet)+1):
        if s[i-1] == alphabet[j-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])

c = table[len(s)][len(alphabet)]
print(26 - c)   