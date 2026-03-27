# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

cointypecount, total = map(int, input().split())
cointype = [int(input().strip()) for i in range(cointypecount)]
cointype = cointype[::-1]

result = 0
for coin in cointype:
    result += (total // coin)
    total %= coin

print(result)