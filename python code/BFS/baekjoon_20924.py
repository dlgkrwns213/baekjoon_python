# https://www.acmicpc.net/problem/20924
import sys
from collections import deque
input = sys.stdin.readline


def get_wood_length() -> (int, int):
    visited[r] = 1
    if len(graph[r]) >= 2:  # 부모가 없으므로 2명 이상의 자식일 경우만
        return r, 0

    q = deque()
    q.append((r, 0))

    while q:
        now, length = q.popleft()
        if len(graph[now]) > 2:  # 부모 + 2명 이상의 자식
            return now, length

        for nxt, nxt_length in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append((nxt, length+nxt_length))

    return now, length  # 기가 노드가 없는 경우


# bfs
def get_branch_length() -> int:
    q = deque()
    q.append((giga_node, 0))

    m = 0
    while q:
        now, length = q.popleft()
        m = max(m, length)

        for nxt, nxt_length in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append((nxt, length+nxt_length))

    return m


n, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

visited = [0] * (n+1)  # 하나의 트리이므로 visited는 공유한다
giga_node, wood_length = get_wood_length()
print(wood_length, get_branch_length())