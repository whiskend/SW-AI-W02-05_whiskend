# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]

# s = "leetcode"
# wordDict = ["leet","code"]

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j] == True:
                    dp[i] = True

        return dp[n]

# 그리디로 풀어서 실패한 케이스
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # +를 사용해서 문자열을 잇는다
#         # 최종 value는 s
#         # 일렬로 늘어진 것은 wordDict의 요소들
#         # 선택은 많다. 따라서 반복문을 돌면서 리스트를 순회한다.
#         # 모든 상태를 저장해 놓을 
#         # s를 매번 찢어서 그 찢은 부분이 wordDict에 있는지 비교한다.
#         # 앞에서부터 찢어가면서 찢는데 성공하고 마지막으로 s가 null값이면 True를 반환한다.
#         for start in range(0, len(s)):
#             for end in range(start, len(s)+1):
#                 if s[start:end] in wordDict:
#                     s = s[end:]

#         if len(s) == 0:
#             return True
#         else:
#             return False
