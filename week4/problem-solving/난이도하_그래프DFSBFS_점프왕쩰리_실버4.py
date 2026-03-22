# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173 

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    # 도착점 도달
    if x == n - 1 and y == n - 1:
        return True

    visited[x][y] = True
    jump = board[x][y]

    # 아래로 점프
    nx, ny = x + jump, y
    if nx < n and not visited[nx][ny]:
        if dfs(nx, ny):
            return True

    # 오른쪽으로 점프
    nx, ny = x, y + jump
    if ny < n and not visited[nx][ny]:
        if dfs(nx, ny):
            return True

    return False

print("HaruHaru" if dfs(0, 0) else "Hing")