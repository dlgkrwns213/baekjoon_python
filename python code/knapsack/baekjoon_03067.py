# https://www.acmicpc.net/problem/14728
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    want = int(input())

    # unbounded knapsack
    dp = [0] * (want+1)  # 1차원 배열 설정
    for coin in coins:
        dp[coin] += 1
        for j in range(1, want+1):
            if j >= coin:
                dp[j] += dp[j-coin]

    print(dp[want])