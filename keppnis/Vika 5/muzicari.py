T, N = map(int, input().split())
a = list(map(int, input().split()))

solution = [[0 for _ in range(T+1)] for _ in range(N+1)]
mark = [[False for _ in range(T+1)] for _ in range(N+1)]

for j in range(T+1):
    solution[0][j] = -j
for i in range(1, N+1):
    for j in range(T+1):
        if a[i-1] <= j and solution[i-1][j] - 1 < solution[i-1][j-a[i-1]]:
            solution[i][j] = solution[i-1][j-a[i-1]]
            mark[i][j] = True
        else:
            solution[i][j] = solution[i-1][j] - 1

belong = [0] * N
ii, jj = N, T
while ii and jj:
    if mark[ii][jj]:
        belong[ii-1] = 1
        jj -= a[ii-1]
    ii -= 1

one, two = 0, 0
for i in range(N):
    if belong[i] == 1:
        print(one, end=' ')
        one += a[i]
    else:
        print(two, end=' ')
        two += a[i]
print()
