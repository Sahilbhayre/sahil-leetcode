class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1

        if n<1:
            return False
        
        nums.sort()

        base = list(range(1, n)) + [n, n]

        return nums == base