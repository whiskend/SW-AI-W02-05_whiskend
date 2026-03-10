# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

from itertools import permutations

def solution():
    N = int(input())
    A = list(map(int, input().split()))

    print(A)
    answer = -float('inf')
    for p in permutations(A):
        result = 0
        for i in range(2, N+1):
            result += abs(p[i-2] - p[i-1])
        answer = max(answer, result)

    print(answer)

if __name__ == "__main__":
    solution()