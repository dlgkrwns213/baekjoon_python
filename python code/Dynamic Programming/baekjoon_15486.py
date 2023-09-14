# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline

n = int(input())
days = [list(map(int, input().split())) for _ in range(n)]

# day를 1일부터 하기 위하여 끝나는 날의 다음날을 기준으로 시작 날을 추가함
start_days = [[] for _ in range(n+1)]
for day, counseling in enumerate(days):
    date, _ = counseling
    finish = day + date
    if finish <= n:
        start_days[finish].append(day)

dp = [0] * (n+1)  # dp[k] : k일까지 벌었던 돈 중 가장 많은 급여
for i in range(n+1):
    dp[i] = dp[i-1]
    for start in start_days[i]:
        dp[i] = max(dp[i], dp[start] + days[start][1])

print(dp[-1])