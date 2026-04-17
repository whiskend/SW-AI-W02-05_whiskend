# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
""" def find():
    N = int(input())
    text = [input().strip() for _ in range(N)]

    for word in text:
        if word[::-1] in text:
            return len(word), word[len(word)//2]

if __name__ == "__main__":
    print(*find()) """

def solve(N, words):
    # 단어들을 돌면서 다른 단어와 비교
    for word1 in words:
        # print(f"첫 번째 반복문: {word1}")
        for word2 in words:
            # print(f"두 번째 반복문: {word2}")
            if(word1 == word2[::-1]):
                print(len(word1), word1[len(word1)//2])
                return

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    words = [input().strip() for _ in range(N)]

    solve(N, words)