# https://www.acmicpc.net/problem/17394
import sys
from collections import deque
input = sys.stdin.readline
MAX = int(1e5)+1


def bfs():
    def fingering(people):  # 핑거 스냅 했을때 결과
        return people // 3, people // 2, people + 1, people - 1

    m = max(n, b) + 1  # 핑거 스냅을 했을때 현재수의 배수로 만들지 않으므로 n과 b중 큰것까지만 확인
    q = deque()
    visited = [0] * m

    q.append((n, 0))
    visited[n] = 1

    while q:
        now, cnt = q.popleft()
        if now in primes:
            return cnt

        for nxt in fingering(now):
            if nxt < 0 or nxt >= m:
                continue
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append((nxt, cnt + 1))

    return -1


is_prime = [1] * MAX
is_prime[0], is_prime[1] = 0, 0
for i in range(2, MAX):
    if is_prime[i]:
        for j in range(i+i, MAX, i):
            is_prime[j] = 0

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    primes = {num for num in range(a, b+1) if is_prime[num]}  # a이상 b이하의 소수 설정
    print(bfs() if primes else -1)