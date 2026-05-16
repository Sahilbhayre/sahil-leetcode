class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low<high:
            mid = (low + high) // 2

            # Case 1
            if nums[mid] > nums[high]:
                low = mid + 1
            
            # Case 2
            elif nums[mid] < nums[high]:
                high = mid
            
            #Case 3:
            else:
                high -= 1

        return nums[low]