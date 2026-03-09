# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

if __name__ == "__main__":
    nums = []
    for _ in range(9):
        nums = input()

    for i in range(9):
        for j in range(9):
            if nums[j] >= nums[j]:
                Max = nums[j]

    print(Max)