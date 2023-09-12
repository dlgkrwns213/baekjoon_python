# https://www.acmicpc.net/problem/1022
def get_nums(x, y):
    level = max(abs(x), abs(y))
    m = (2 * level + 1) ** 2

    if x == level:
        return m - (level - y)
    elif y == -level:
        m -= 2 * level
        return m - (level - x)
    elif x == -level:
        m -= 4 * level
        return m - (level + y)
    else:
        m -= 6 * level
        return m - (level + x)


r1, c1, r2, c2 = map(int, input().split())
ans = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        ans[i-r1][j-c1] = get_nums(i, j)

# 이쁘게 print
max_length = max(len(str(num)) for row in ans for num in row)
for row in ans:
    print(' '.join(map(lambda num: (' '*max_length+str(num))[-max_length:], row)))

