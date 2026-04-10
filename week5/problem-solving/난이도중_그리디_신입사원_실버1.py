# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

score = [(3, 6),(7, 3),(4, 2),(1, 4),(5, 7),(2, 5),(6, 1)]
# print([item[0] for item in score])

row0 = sorted(score, key = lambda item: item[0], reverse = True)
row1 = sorted(score, key = lambda item: item[1], reverse = True)
print(row0)
print(row1)

if row0[0] 