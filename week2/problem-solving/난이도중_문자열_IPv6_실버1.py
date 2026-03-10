# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

def decoding(summary):
    if "::" in summary:
        left, right = summary.split('::')
        left = left.split(':') if left else []
        right = right.split(':') if right else [] # [1, 1985, aa25, ...]

        missing = 8 - len(left) - len(right)

        parts = left + ['0000']*missing + right

    else:
        parts = summary.split(':')

    for i in range(8):
        parts[i] = parts[i].zfill(4)

    print(':'.join(parts))

    
if __name__ == "__main__":
    summary = input()
    decoding(summary)