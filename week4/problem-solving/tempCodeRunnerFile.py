# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 7                           
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
from collections import deque
start = 1
queue = deque([start])

node_num = int(input())
edge_num = int(input())
graph = [[]for _ in range(node_num+1)]

for _ in range(edge_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = list([False] * (node_num+1))

count = 0
while queue:
    current = queue.popleft()
    count += 1
    for i in graph[current]:
        if not visited[i]:
            visited = True
            queue.extend(i)