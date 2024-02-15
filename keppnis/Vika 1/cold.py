n = int(input())
count = 0
t = input().split()
for numbers in t:
    if int(numbers) < 0:
        count += 1

print(count)

