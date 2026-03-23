# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
# 입력으로 '노드개수'와 '리프개수'를 받는다.
n, m = map(int, input.split())
# 간선 변수를 초기화한다.
edges = []
# 0을 시작으로 '리프개수'만큼 노드를 붙인다.
for i in range(1, m+1):
    edges.append([0, i])
# 1에서 시작해 체인 구조로 나머지 노드를 이어 붙인다.
prev = 0
for i in range(m+1, n+1):
    edges.append([prev, i])
# 출력한다.
for i in range(len(edges)):
    print(edges[i])