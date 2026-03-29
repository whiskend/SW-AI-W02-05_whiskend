class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [0] * n
        # i 번째 집까지만 있을 때 최대 금액 

        # 집 건너뛰는 건 2개 까지가 최대이므로 0 ~ 3까지만 base case 설정 
        # ex) 2 7 9 3 1

        if n >= 1:
            dp[0] = nums[0]
        if n >= 2:
            dp[1] = max(dp[0], nums[1])
        if n >= 3:
            dp[2] = max(dp[0] + nums[2], nums[1])
        if n >= 4:
            dp[3] = max(dp[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])
            # 0 2 번째 vs 1 3 번째 vs 0 3 번째 
        
        if n >= 5:
            for i in range(4, len(nums)): 
                dp[i] = max(dp[i - 3] + nums[i], dp[i - 2] + nums[i], dp[i - 1])
                # 2개까지 최대 + 5번째 
                # 3개까지 최대 + 5번째
                # 4개까지 최대 

        return dp[n - 1]