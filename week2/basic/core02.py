class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        answer = []
        def backtracking(index, result):
            if(index == len(digits)):
                answer.append("".join(result))
                return

            for c in letter[digits[index]]:
                result.append(c)
                backtracking(index + 1, result)
                result.pop()

        backtracking(0,[])
        return answer