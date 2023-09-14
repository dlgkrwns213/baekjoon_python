# https://www.acmicpc.net/problem/7579
n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 0-1 knapsack
total = sum(costs)
dp = [[0]*(total+1) for _ in range(n)]
for i in range(n):
    memory, cost = memories[i], costs[i]
    for j in range(1, total+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory)

for cost, memory in enumerate(dp[-1]):
    if memory >= m:
        print(cost)
        break