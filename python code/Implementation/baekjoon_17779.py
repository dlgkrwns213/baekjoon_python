# https://www.acmicpc.net/problem/17779
import sys
input = sys.stdin.readline


def get_citizen_gap():
    one, two, three, four = 0, 0, 0, 0

    # one two
    for i in range(x):
        one += sum(people[i][:y+1])
        two += sum(people[i][y+1:])

    # one
    for i in range(d1):
        one += sum(people[x+i][:y-i])

    # two
    for i in range(d2+1):
        two += sum(people[x+i][y+i+1:])

    # three
    for i in range(d2+1):
        three += sum(people[x+d1+i][:y-d1+i])

    # four
    for i in range(d1):
        four += sum(people[x+d2+1+i][y+d2-i:])

    for i in range(x+d1+d2+1, n):
        three += sum(people[i][:y-d1+d2])
        four += sum(people[i][y-d1+d2:])

    citizens = [one, two, three, four]
    citizens.append(total - sum(citizens))  # five
    return max(citizens) - min(citizens)


n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
total = sum(map(sum, people))

m = float('inf')
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if y - d1 < 0 or x + d1 + d2 >= n or y + d2 >= n:
                    continue
                m = min(m, get_citizen_gap())

print(m)