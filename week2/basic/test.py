# nums에 주어진 숫자들로 만들 수 있는 경우의 수를 순서를 고려하여 출력
nums = [1, 2, 3]
path = []

def backtrack():

    # ① 종료 조건
    if len(path) == len(nums):
        print(path)
        return

    # ② 선택지 탐색
    for n in nums:
        if n in path:
            continue

        # ③ 선택
        path.append(n)

        # ④ 다음 단계 탐색
        backtrack()

        # ⑤ 선택 취소 (Backtracking)
        path.pop()

if __name__ == "__main__":
    backtrack()