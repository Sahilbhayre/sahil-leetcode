class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = int((n * (n + 1)) / 2)
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        