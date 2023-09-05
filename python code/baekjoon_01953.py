# https://www.acmicpc.net/problem/1953
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, start_team_num):
    visited[start] = 1

    q = deque()
    q.append((i, start_team_num))

    while q:
        person, team_num = q.popleft()
        teams[team_num].append(person)
        for hate_person in graph[person]:
            if visited[hate_person]:
                continue

            visited[hate_person] = 1
            q.append((hate_person, not team_num))


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    cnt, *people = map(int, input().split())
    for j in people:
        graph[i+1].append(j)

# bfs
teams, num, visited = [[] for _ in range(2)], 0, [0] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(i, num)
        num = not num

# team 정렬 후 출력
for team in teams:
    team.sort()
    print(len(team))
    print(' '.join(map(str, team)))
