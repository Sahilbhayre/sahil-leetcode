class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for j in range(1, n):
            for i in range(j):
                if -target <= nums[j] - nums[i] <= target:
                    if dp[i] != -1:
                        dp[j] = max(dp[j], dp[i] + 1)
        return dp[n-1]
