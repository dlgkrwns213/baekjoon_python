# https://www.acmicpc.net/problem/9702
import sys
input = sys.stdin.readline


def bisect_left(parts, val):
    left, right = 0, len(parts)
    while left < right:
        mid = left + right >> 1
        if parts[mid] < val:
            left = mid + 1
        else:
            right = mid
    return left


for testcase in range(int(input())):
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    total = 0
    for start in range(n):
        # start 부터 시작하여 LIS 구하기
        longest_parts, length = [], 0
        for idx in range(start, n):
            if not longest_parts or nums[idx] > longest_parts[-1]:
                longest_parts.append(nums[idx])
                length += 1
            elif nums[idx] < longest_parts[-1]:
                longest_parts[bisect_left(longest_parts, nums[idx])] = nums[idx]
            total += length

    print(f'Case #{testcase+1}: {total}')