# https://www.acmicpc.net/problem/17845
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
studies = [list(map(int, input().split())) for _ in range(k)]

# 0-1 knapsack
dp = [[0]*(n+1) for _ in range(k)]  # 2차원 배열 설정
for i, study in enumerate(studies):
    weight, needs_time = study
    for time in range(1, n+1):
        if time < needs_time:
            dp[i][time] = dp[i-1][time]
        else:
            dp[i][time] = max(dp[i-1][time], dp[i-1][time-needs_time]+weight)

print(dp[k-1][n])