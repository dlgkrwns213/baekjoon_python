# https://www.acmicpc.net/problem/13398
n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
if nums[0] > 0:
    dp[0][0], dp[0][1] = nums[0], nums[0]

for i, v in enumerate(nums):
    if i == 0:
        continue

    if v > 0:
        dp[i][0], dp[i][1] = dp[i-1][0] + v, dp[i-1][1] + v  # 양수일 경우 무조건 더하기
    else:
        if dp[i-1][0] + v > 0:  # 기존과 동일한 방법
            dp[i][0] = dp[i-1][0] + v

        dp[i][1] = max(dp[i-1][1] + v, dp[i-1][0])  # 현재 수를 삭제하는 것과 기존에 삭제하여 더한 것의 크기를 비교

ans = max(map(max, dp))
print(ans if ans != 0 else max(nums))  # 모두 음수일 경우 수를 하나도 고르지 않게 되므로 최대값 하나만 선택