# https://www.acmicpc.net/problem/20303
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(rep, now):
    group[rep] += candies[now]
    group_cnt[rep] += 1
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(rep, nxt)


n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 한 아이의 사탕을 뻇으면 그 그룹의 모든 아이의 사탕을 뺴앗아야 하므로 그룹별로 묶어줌 (사탕 개수, 명수)
visited, group, group_cnt = [0] * (n+1), dict(), dict()
for i in range(1, n+1):
    if not visited[i]:
        visited[i], group[i], group_cnt[i] = 1, 0, 0
        dfs(i, i)

# dict -> list 로 변경
group = [v for i, v in sorted(group.items())]
group_cnt = [v for i, v in sorted(group_cnt.items())]

# 0-1 knapsack
length = len(group)
dp = [[0]*k for _ in range(length)]
for i in range(length):
    weight, count = group[i], group_cnt[i]
    for j in range(1, k):
        if j < count:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-count] + weight)

print(dp[length-1][k-1])  # 울음소리가 k여도 안됨
