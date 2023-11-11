# https://www.acmicpc.net/problem/10422
MOD = int(1e9) + 7
dp = [0] * 2501
dp[0], dp[1] = 1, 1  # '', ()

for i in range(2, 2501):
    dp[i] = sum(map(lambda j: dp[i-j-1]*dp[j] % MOD, range(i))) % MOD
    '''
    dp[i]
    j번째 : [dp[j]dp[i-j-i]
    
    EX)
    dp[3]
    [dp[0]]dp[2] : [](()) []()()
    [dp[1]]dp[1] : [()]()
    [dp[2]]dp[0] : [(())] [()()]
    
    dp[4]
    [dp[0]]dp[3] : []()(()) []()()() [](())() []((())) [](()())
    [dp[1]]dp[2] : [()](()) [()]()()
    [dp[2]]dp[1] : [(())]() [()()]()
    [dp[3]]dp[0] : [()(())] [()()()] [(())()] [((()))] [(()())]
    '''

ans = []
for _ in range(int(input())):
    n = int(input())
    if n % 2:
        ans.append(0)
    else:
        ans.append(dp[n >> 1])

print('\n'.join(map(str, ans)))