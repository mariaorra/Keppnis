n = int(input())
c = []

for _ in range(n):
    c.extend(map(int, input().split()))

c.sort(reverse=True)

h = 0
for i, c in enumerate(c, start=1):
    if c >= i:
        h = i
    else:
        break

print(h)