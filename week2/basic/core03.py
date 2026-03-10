# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = float(1)
    
        if n > 0:
            for _ in range(n):
                answer *= x

        elif n == 0:
            return answer

        else:
            n *= -1
            x = 1 / x
            for _ in range(n):
                answer *= x

        return answer