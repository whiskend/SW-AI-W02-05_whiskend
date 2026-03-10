# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

def Nqueen():
    N = int(input())
    count = 0

    cols = [False] * N                  # 같은 열 사용 여부
    diag1 = [False] * (2 * N - 1)      # row - col + (N - 1)
    diag2 = [False] * (2 * N - 1)      # row + col

    def dfs(row):
        nonlocal count

        if row == N:
            count += 1
            return

        for col in range(N):
            d1 = row - col + (N - 1)
            d2 = row + col

            if cols[col] or diag1[d1] or diag2[d2]:
                continue

            cols[col] = True
            diag1[d1] = True
            diag2[d2] = True

            dfs(row + 1)

            cols[col] = False
            diag1[d1] = False
            diag2[d2] = False

    dfs(0)
    print(count)

if __name__ == "__main__":
    Nqueen()