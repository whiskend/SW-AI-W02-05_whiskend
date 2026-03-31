# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

# N, K  = 4, 7
# items = [(6, 13), (4, 8), (3, 6), (5, 12)]

N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [0] * (K + 1)

for weight, value in items:
    print(f"\n\n\nweight: {weight} value: {value}\n----------------------------\n")
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
        print(w)
        print(dp)
