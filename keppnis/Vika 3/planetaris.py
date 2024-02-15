n, a = map(int, input().split())

ships = list(map(int, input().split()))
if len(ships) != n:
        exit()

ships.sort()
k = 0

if n == 0 or a == 0:
     exit()

for ship in ships:
    if a > ship:
        k += 1
        a -= (ship + 1)
    else:
        break
print(k)