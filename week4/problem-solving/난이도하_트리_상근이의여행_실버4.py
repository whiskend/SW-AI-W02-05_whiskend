# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

T = int(input())
for _ in range(T):
    node_num, edges_num = map(int, input().split())
    edges = []
    for _ in range(edges_num):
        a, b = map(int, input().split())
    print(node_num - 1)
    
# 1. dfs로 순회한다. 어떻게? edge에 연결된 노드를 다믕 dfs로 넘겨준다.
# 2. dfs(start=1, end=1의따까리) return count += 1
# 3. count_list.append(count)
# 4. Return max(count_list)