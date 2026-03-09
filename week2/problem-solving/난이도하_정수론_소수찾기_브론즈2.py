# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

def find_primary(num, count):
    for _ in range(num):
        number = int(input())

        if number == 1:
            continue

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            count += 1
    return count


if __name__ == "__main__":
    num = int(input())
    count = 0

    print(find_primary(num, count))