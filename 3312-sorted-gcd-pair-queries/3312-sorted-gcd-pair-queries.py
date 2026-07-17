from typing import List
import collections
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: Count frequency of each number in nums
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
            
        # Step 2: Compute cnt[i] -> count of numbers divisible by i
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += freq[j]
                
        # Step 3: Compute exact[i] -> count of pairs with GCD exactly equal to i
        exact = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            # Total pairs where both elements are divisible by i
            total_pairs = cnt[i] * (cnt[i] - 1) // 2
            
            # Subtract pairs where the GCD is a strict multiple of i
            for j in range(2 * i, max_val + 1, i):
                total_pairs -= exact[j]
            
            exact[i] = total_pairs
            
        # Step 4: Build prefix sums of exact GCD counts
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i - 1] + exact[i]
            
        # Step 5: Answer each query using binary search
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q)
            ans.append(idx)
            
        return ans