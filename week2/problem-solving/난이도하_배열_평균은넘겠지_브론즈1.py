# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    number = list(map(int, input().split()))
    N2 = number[0]
    scores = number[1:]
    
    sum = 0
    for score in scores:
        sum += score
    mean = sum/len(scores)

    high = 0
    for score in scores:
        if score > mean:
            high += 1
    x = high/len(scores)*100
    print(f"{x:.3f}%")
    