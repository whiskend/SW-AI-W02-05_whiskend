# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

from collections import deque

n = int(input())

# 연결 정보를 저장할 인접 리스트
ednges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    ednges[u].append(v)
    ednges[v].append(u)

# 부모 노드 번호를 저장할 리스트 (0으로 초기화)
parents = [0] * (n + 1)

# 2. 1번 노드부터 탐색 시작 (BFS)
queue = deque([1])
parents[1] = -1  # 1번은 루트이므로 부모가 없다는 표시 (방문 처리 겸용)

while queue:
    current = queue.popleft()
    
    # 현재 노드와 연결된 친구들을 확인
    for neighbor in ednges[current]:
        # 아직 부모가 결정되지 않았다면 (방문하지 않았다면)
        if parents[neighbor] == 0:
            parents[neighbor] = current  # '나'가 이 친구의 부모가 됨
            queue.append(neighbor)      # 다음 탐색을 위해 큐에 삽입

# 3. 2번 노드부터 부모 번호 출력
for i in range(2, n + 1):
    print(parents[i])