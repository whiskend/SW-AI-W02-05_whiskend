# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

goal, impossibilitys_num = map(int, input().split())
impossibilitys = [int(input()) for _ in range(impossibilitys_num)] #갈 수 없는 돌
# print(f"goal: {goal} impossibilitys_num:{impossibilitys_num} impossibilitys {impossibilitys}")
canvisited = [True for _ in range(goal)]
for i in range(goal):
    if i in impossibilitys:
        canvisited[i] = False # 갈 수 없는 돌은 False. 밑에 if문에서 거름

jump_num = int((2*goal) ** 0.5 + 2) # 최대 점프 칸 수 계산
# print(f"jump_num: {jump_num}")
dp = [[float('inf') for _ in range(jump_num+2)] for _ in range(goal+1)] # inf로 구성된 jump_num x goal 행렬 생성
# print(dp)

dp[1][1] = float('inf')
dp[2][1] = 1

if canvisited[i]:
    for i in range(3, goal+1):
            # if i <= jump_num+1:
            #     for j in range(1, 3):        
            #         dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1])
            # else:
                for j in range(1, jump_num+1):        
                    # print(f"i: {i}, j: {j}")
                    dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
# for i in range(1, goal+1):
#     print(dp[i])
print(min(dp[goal]))