class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)

        return (max_val - min_val) * k