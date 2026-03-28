# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

N = int(input())

def tile(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    n_2 = 1
    n_1 = 2
    for _ in range(3, N+1):
        temp = n_1 + n_2
        n_2 = n_1
        n_1 = temp % 15746
        print(f"n_1: {n_1} n_2: {n_2} for: temp: {temp}")

    return n_1

print(tile(N))