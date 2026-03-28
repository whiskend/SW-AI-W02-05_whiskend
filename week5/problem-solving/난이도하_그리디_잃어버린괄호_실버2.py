# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

equation = input()

# 마아너스 제거하고 리스트에 넣음
nominus_equation = equation.split("-")

# 리스트의 아이템 중에 '40+50' 같은 것들을 합쳐버린다. 90으로
curr_list = []
sum_list = []
for i in range(len(nominus_equation)):
    curr_list = list(map(int, nominus_equation[i].split("+")))
    sum_list.append(sum(curr_list))

# 첫 번째 item에서  -와 - 사이에 있는 값들을 다 더한 것들을 전부 빼준다
ans = sum_list[0]
for i in range(1, len(sum_list)):
    ans -= sum_list[i]

print(ans)