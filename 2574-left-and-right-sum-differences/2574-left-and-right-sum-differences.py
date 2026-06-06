class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_sum = 0
        right_sum = sum(nums)
        answer = []

        for num in nums:
            right_sum -= num

            answer.append(abs(left_sum - right_sum))

            left_sum += num
        return answer