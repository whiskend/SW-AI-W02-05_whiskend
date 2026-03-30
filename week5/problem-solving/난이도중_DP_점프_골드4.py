# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

goal, impossibilitys_num = map(int, input().split())
impossibilitys = [int(input()) for _ in range(impossibilitys_num)] #갈 수 없는 돌
canvisited = [True for _ in range(goal+1)]
for i in range(goal):
    if i in impossibilitys:
        canvisited[i] = False # 갈 수 없는 돌은 False. 밑에 if문에서 거름

jump_num = int((2*goal) ** 0.5 + 2) # 최대 점프 칸 수 계산
dp = [[float('inf') for _ in range(jump_num+2)] for _ in range(goal+1)] # inf로 구성된 jump_num x goal 행렬 생성

if canvisited[2]:
    dp[1][1] = float('inf')
    dp[2][1] = 1
    
    for i in range(3, goal+1):
        if canvisited[i]:
            for j in range(1, jump_num+1):        
                dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
    # for i in range(1, goal+1):
    #     print(dp[i])
    ans = min(dp[goal])
    if ans != float('inf'):
        print(min(dp[goal]))
    else:
        print(-1)

else:
     print(-1)