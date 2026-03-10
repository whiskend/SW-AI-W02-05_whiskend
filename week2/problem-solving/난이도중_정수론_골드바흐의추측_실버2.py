# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020
# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


if __name__ == "__main__":
    t = int(input())
    nums = [int(input()) for _ in range(t)]

    max_n = max(nums)
    prime_check = sieve(max_n)

    for n in nums:
        left = n // 2

        while left > 1:
            right = n - left

            if prime_check[left] and prime_check[right]:
                print(left, right)
                break

            left -= 1