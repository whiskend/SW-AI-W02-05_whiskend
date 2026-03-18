# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
def find():
    N = int(input())
    text = [input().strip() for _ in range(N)]

    for word in text:
        if word[::-1] in text:
            return len(word), word[len(word)//2]

if __name__ == "__main__":
    print(find())