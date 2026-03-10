# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

def hanoi(N, fr, mid, to):
    
    if (N == 1):
        print(fr + " " + to)
        return

    hanoi(N - 1, fr, to, mid)
    print(fr + " " + to)
    hanoi(N - 1, mid, fr, to)

def hanoi_count(N):
    if N == 1:
        return 1
    return hanoi_count(N-1)*2 + 1

if __name__ == "__main__":
    N = int(input())
    print(hanoi_count(N))
    if not N > 20:
        hanoi(N, "1", "2", "3")