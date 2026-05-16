class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        
        # Step 1: Compute suffix minimums
        # suff_min[i] will store the minimum value from index i to n-1
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        ans = [0] * n
        
        # Step 2: Iterate through the array to find components using prefix maximum
        start = 0
        current_max = nums[0]
        
        for i in range(n):
            current_max = max(current_max, nums[i])
            
            # A component boundary/cut is valid if we reached the end of the array,
            # or if the maximum value seen so far in this component is <= the minimum of the remaining suffix.
            if i == n - 1 or current_max <= suff_min[i + 1]:
                # All elements from 'start' to 'i' belong to the same component.
                # Their maximum reachable value is 'current_max'.
                for j in range(start, i + 1):
                    ans[j] = current_max
                
                # Reset for the next component
                if i < n - 1:
                    start = i + 1
                    current_max = nums[start]
                    
        return ans        