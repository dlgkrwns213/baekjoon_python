n = int(input())
for _ in range(n):
    tc = int(input())
    dp = [[0, 0] for _ in range(tc+1)]
    if tc==0:
        print(1, 0)
        continue
    dp[0], dp[1] = [1, 0], [0, 1]
    for i in range(2, tc+1):
        dp[i][0], dp[i][1] = dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]
    print(dp[tc][0], dp[tc][1])
