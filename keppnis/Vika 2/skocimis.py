abc = input().split(" ")
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

count = 0

while c - b > 1 or b - a > 1:
    ab = b - a
    bc = c - b
    if ab > bc:
        c = b
        b = a + 1
        count += 1
    else:
        a = b
        b = c - 1
        count += 1

print(count)