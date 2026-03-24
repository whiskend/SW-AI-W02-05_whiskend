# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

from collections import deque

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))

visited = [-1] * (k + 1)
queue = deque([0])
visited[0] = 0

while queue:
    current = queue.popleft()

    for coin in coins:
        next_value = current + coin

        if next_value > k:
            continue

        if visited[next_value] == -1:
            visited[next_value] = visited[current] + 1
            queue.append(next_value)

print(visited[k])