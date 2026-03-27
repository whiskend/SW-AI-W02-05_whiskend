# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        if n == 1:
            return 1
        if n == 2:
            return 2
            
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]