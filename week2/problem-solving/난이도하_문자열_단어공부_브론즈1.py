# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

def MaxAlphabet(s):
    s = s.upper()
    count_dict = {}
    
    for c in s:
        count_dict[c] = count_dict.get(c, 0) + 1

    Max = max(count_dict.values())

    if list(count_dict.values()).count(Max) > 1:
        print("?")
    else:
        for k, v in count_dict.items():
            if v == Max:
                print(k)


if __name__ == "__main__":
    s = input()
    MaxAlphabet(s)