n = int(input())

a = list(map(int, input().split(" ")))
if len(a) != n:
        exit()

a.sort()
s = 0

for j in range(n-1):
        #s = ((a1 - a2)**2 for a1, a2 in zip(a, a[1:]))
        s += (a[j] - a[j+1])**2

print(s)