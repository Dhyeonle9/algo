import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    dp = [0] * (N+1)
    dp[1], dp[2], dp[3] = 1, 2, 4
    for j in range(4, N+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    print(dp[N])