# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque
N = int(input())

# 입력 받은 숫자만큼 반복문으로 큐에 집어넣기
q = deque()
for i in range(1,N+1):
    q.append(i)

# 큐에서 하나 빼서 버리고, 하나 뺏다가 다시 넣기
while(len(q) != 1):
    q.popleft()
    q.append(q.popleft())

x = q.popleft()
print(x)