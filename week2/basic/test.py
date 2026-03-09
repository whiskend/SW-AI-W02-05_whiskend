n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
answer = float('inf')

def dfs(start, now, visited_count, cost):
    global answer

    # 가지치기
    if cost >= answer:
        return

    # 모든 도시 방문
    if visited_count == n:
        if W[now][start] != 0:
            answer = min(answer, cost + W[now][start])
        return

    for next in range(n):
        if not visited[next] and W[now][next] != 0:
            visited[next] = True
            dfs(start, next, visited_count + 1, cost + W[now][next])
            visited[next] = False

# 시작 도시를 0으로 고정
visited[0] = True
dfs(0, 0, 1, 0)

print(answer)













# # nums에 주어진 숫자들로 만들 수 있는 경우의 수를 순서를 고려하여 출력
# nums = [1, 2, 3]
# path = []

# def backtrack():

#     # ① 종료 조건
#     if len(path) == len(nums):
#         print(path)
#         return

#     # ② 선택지 탐색
#     for n in nums:
#         if n in path:
#             continue

#         # ③ 선택
#         path.append(n)

#         # ④ 다음 단계 탐색
#         backtrack()

#         # ⑤ 선택 취소 (Backtracking)
#         path.pop()

# if __name__ == "__main__":
#     backtrack()