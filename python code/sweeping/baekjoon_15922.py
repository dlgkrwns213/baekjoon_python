# https://www.acmicpc.net/problem/15922
import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

total = 0
start, finish = lines[0]
for x, y in lines[1:]:
    # 이전 선분과 연결되지 않는 경우
    if x > finish:
        total += finish - start
        start, finish = x, y
    # 이전 선분과 연결되는 경우
    else:
        finish = max(finish, y)

# 마지막은 적용이 안되었으므로 추가로 더해준다.
print(total + finish - start)