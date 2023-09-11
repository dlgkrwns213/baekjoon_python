# https://www.acmicpc.net/problem/1106
import sys
input = sys.stdin.readline
INF = sys.maxsize

c, n = map(int, input().split())
ads = [list(map(int, input().split())) for _ in range(n)]

dp = [INF] * 1100
for cost, customer in ads:
    dp[customer] = min(dp[customer], cost)

for i in range(1100):
    for cost, customer in ads:
        if i >= customer:
            dp[i] = min(dp[i], dp[i-customer]+cost)

print(min(dp[c:]))