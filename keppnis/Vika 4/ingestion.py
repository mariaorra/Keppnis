def calc_cal(n, m):
    if n >= len(calories):
        return 0
    if max_cal[n][m] != -1:
        return max_cal[n][m]
    total = calc_cal(n + 1, m * 2 // 3 if n else m)
    total = max(total, calc_cal(n + 2, m))
    total = max(total, calc_cal(n + 3, M))
    total += min(calories[n], m)
    max_cal[n][m] = total
    return total


n, M = map(int, input().split())
calories = [0] + list(map(int, input().split()))

max_cal = [[-1 for _ in range(M + 1)] for _ in range(n + 1)]
print(calc_cal(0, M))

