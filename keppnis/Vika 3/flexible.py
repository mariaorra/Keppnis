w, p = map(int, input().split())
partitions = list(map(int, input().split()))
if len(partitions) != p:
    exit()

width = set()
width.add(w)

for i in range(len(partitions)):
    width.add(partitions[i])
    width.add(w - partitions[i])

    for j in range(i + 1, len(partitions)):
        width.add(partitions[j] - partitions[i])

k = sorted(width)
print(*k)