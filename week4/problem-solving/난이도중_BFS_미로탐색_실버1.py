# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue

            # 아직 방문 안 한 길이면
            if not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))