# https://www.acmicpc.net/problem/4811
import sys
input = sys.stdin.readline

counts = [[0] * 31 for _ in range(31)]  # i개의 'W' 와 j개의 'H'를 사용하여 만들수 있는 문자열 개수
for i in range(1, 31):
    counts[i][0] = 1  # 'W'가 무조건 먼저 시작
    for j in range(1, i+1):
        counts[i][j] = counts[i-1][j] + counts[i][j-1]

ans = []
while 1:
    n = int(input())
    if not n:
        break

    ans.append(counts[n][n])

print('\n'.join(map(str, ans)))