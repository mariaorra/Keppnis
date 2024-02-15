n, k = map(int, input().split())
if n < k:
        exit()
w = list(map(int, input().split()))
if len(w) != n:
        exit()

lowest = max(w) 
highest = sum(w)

while lowest < highest:
        test = (lowest + highest) // 2
        sum = 0
        count = 1
        for weight in w:
                sum += weight
                if sum > test:
                        sum = weight
                        count += 1
        if count <= k:
                highest = test
        else:
                lowest = test + 1

print(lowest)

#boxes = [[] for a in range(k)]
#for i in w:
        #for j in k:
                #j == min(boxes)
                #j += i
#print(max(boxes))