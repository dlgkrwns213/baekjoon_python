# https://www.acmicpc.net/problem/17069
import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]  # 0: 가로 1: 대각 2: 세로
for j in range(1, n):
    if room[0][j]:
        break
    dp[0][j][0] = 1

for i in range(1, n):
    for j in range(1, n):
        if room[i][j]:
            continue

        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

        if not room[i-1][j] and not room[i][j-1]:
            dp[i][j][1] = sum(dp[i-1][j-1])

print(sum(dp[n-1][n-1]))