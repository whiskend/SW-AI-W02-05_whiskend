# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

testEA = int(input())
for _ in range(testEA):
    coinEA = int(input()) # 3
    cointype = list(map(int, input().split())) # 1 5 
    
    target = int(input()) # 100

    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in cointype: #cointype : 1, 2, 5
        for n in range(coin, target+1): # 5, 22
            if dp[n-coin] != 0:
                dp[n] += dp[n-coin]

    print(dp[target])