# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971


if __name__ == "__main__":
    n = input()
    matrix = []
    for _ in range(n):
        row = list(int, map(input().split()))
        matrix.append(row)
    