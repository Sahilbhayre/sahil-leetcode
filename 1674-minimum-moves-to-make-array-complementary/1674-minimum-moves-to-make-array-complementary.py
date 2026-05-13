class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        #diff[i] stores the change in moves required for target sum i
        # Range of target sum is [2, 2*limit]
        diff = [0] * (2*limit + 2)
        n = len(nums)

        for i in range(n // 2):
            a, b = nums[i], nums[n-1-i]

            # If we want a sum in [min(a, b) + 1, max(a, b) + limit],
            # we only need 1 move instead of 2. (Subtract 1 move)
            low = min(a, b) + 1
            diff[2] += 2
            diff[2*limit + 1] -= 2

            low = min(a, b) + 1
            high = max(a, b) + limit
            diff[low] -= 1
            diff[high + 1] += 1

            # If we want the sum to be exactly a + b,
            # we need 0 moves instead of 1. (Subtract 1 more move)
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        # Prefix sum to find the minimum moves among all target sums
        min_moves = n  # Max possible moves is n
        current_moves = 0 
        for i in range(2, 2*limit + 1):
            current_moves += diff[i]
            min_moves = min(min_moves, current_moves)
        
        return min_moves
