# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())
memo = [0] * (n+1)

def dp(n, memo):
    if n == 1:
        return 1
    if n == 2:
        return 1

    result = 0
    if memo[n] != 0:
        result = memo[n]
        return result
    
    result = dp(n-1, memo) + dp(n-2, memo)
    memo[n] = result
    
    return result

print(dp(n, memo))