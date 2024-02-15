def difference(num):
     return abs(1000 - num)

n = int(input())
weights = []
for _ in range(n):
    weights.append(int(input()))

closest = difference(weights[0])

combinations = {weights[0]: weights[0]}

for i in weights[1:]:
    keys = list(combinations.keys())
    if (i < 1000 or difference(i) < best):
         combinations[i] = i

    for j in keys:
        if j > 1000 and closest < difference(j):
            del combinations[j]
        elif (difference(i+j) <= closest):
             combinations[i+j] = i+j
             closest = difference(i+j)
        elif (i+j < 1000):
             combinations[i+j] = i+j
        

num = 1000 + closest
if num in combinations:
     print(num)
else:
     print(1000-closest)

