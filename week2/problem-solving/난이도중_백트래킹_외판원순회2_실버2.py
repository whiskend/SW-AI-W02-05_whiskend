# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

def tsp():
    N = int(input())
    W = list(map(int, input().split()) for _ in range(N))
    
    ans = float('inf')
    visited = [False] * N

    def dfs(start, now, count, cost):
        nonlocal ans
        if count == N:
            if W[now][start] != 0:
                ans = min(ans, cost + W[now][start])
                return
        for nxt in range(N):
            visited[nxt] = True
            dfs(start, nxt, count + 1, cost + W[now][nxt])
            visited[nxt] = False


    for start in N:
        visited[start] = True
        dfs(start, start, 1, 0)
        visited[start] = False

    print(ans)


if __name__ == "__main__":
    tsp()