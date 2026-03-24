# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

n = int(input())
dp = [0] * (n + 1) # dp[i]는 i번째 작업이 '완료'되는 시점의 최소 시간을 저장

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    current_task_time = data[0]
    num_prev_jobs = data[1]
    prev_jobs_list = data[2:]

    if num_prev_jobs == 0:
        dp[i] = current_task_time
    else:
        # 선행 작업들 중 가장 늦게 끝나는 시간
        max_prev_completion_time = 0
        
        for job_id in prev_jobs_list:
            # 이전에 저장된 dp[job_id] 값들 중 최댓값을 갱신
            if dp[job_id] > max_prev_completion_time:
                max_prev_completion_time = dp[job_id]
        
        # (가장 늦게 끝난 선행 작업 시간) + (현재 작업 시간)
        dp[i] = max_prev_completion_time + current_task_time

# 모든 작업 중 가장 마지막에 끝나는 시간 출력
answer = 0
for time in dp:
    if time > answer:
        answer = time
        
print(answer)