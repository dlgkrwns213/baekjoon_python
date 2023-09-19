# https://www.acmicpc.net/problem/29158
from math import log2, sqrt

init = int(input())

# sunghun
# 소인수분해를 위한 prime 설정
n = init

MAX = int(sqrt(n)) + 1
is_prime, primes = [1] * MAX, []
is_prime[0], is_prime[1] = 0, 0
for i in range(MAX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i+i, MAX, i):
            is_prime[j] = 0

# 소인수분해
factors = []
idx, cnt = 0, len(primes)
while idx < cnt:
    num = primes[idx]
    if n % num:
        idx += 1
    else:
        n //= num
        factors.append((str(num), str(num)*20))
if n > 1:
    factors.append((str(n), str(n)*20))

# 문자열을 기준으로 역순 정렬 후 합쳐주기 ('31' < '3' == '33' < '37'의 순서가 되어야 함)
factors.sort(key=lambda factor: factor[1][:20], reverse=True)
real, _ = zip(*factors)
su = ''.join(map(str, real))

# jihun
n = init - 1  # n보다 작은....

if n == 1:
    ji = 1
else:
    x = int(log2(n)) - 1  # 자릿수가 많으면 좋으므로 최대한 2로 나누어야 함 (3 * 3 > 2 * 2 * 2)
    m = 1 << x
    k = n // m

    if k == 3:
        ji = '3' + '2'*x
    elif k == 2:
        ji = '2' * (x+1)
    else:
        ji = '2' * x

print(int(su)+int(ji))
