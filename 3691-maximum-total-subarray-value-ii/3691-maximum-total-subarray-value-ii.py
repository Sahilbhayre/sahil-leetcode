import math
import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

# 1. Build Sparse Table for RMQ (Min and Max)
        max_k = int(math.log(n, 2)) + 1
        st_min = [[0] * n for _ in range(max_k)]
        st_max = [[0] * n for _ in range(max_k)]
        
        for i in range(n):
            st_min[0][i] = nums[i]
            st_max[0][i] = nums[i]
            
        for j in range(1, max_k):
            length = 1 << j
            half_length = 1 << (j - 1)
            for i in range(n - length + 1):
                st_min[j][i] = min(st_min[j - 1][i], st_min[j - 1][i + half_length])
                st_max[j][i] = max(st_max[j - 1][i], st_max[j - 1][i + half_length])
                
        # Precompute log base 2 for O(1) queries
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1
            
        def get_val(l, r):
            if l > r: 
                return 0
            j = log_table[r - l + 1]
            min_val = min(st_min[j][l], st_min[j][r - (1 << j) + 1])
            max_val = max(st_max[j][l], st_max[j][r - (1 << j) + 1])
            return max_val - min_val

        # 2. Priority Queue (Max-Heap)
        # Python's heapq is a min-heap, so we store negative values
        # Tuple structure: (-value, l, r)
        pq = []
        for l in range(n):
            val = get_val(l, n - 1)
            pq.append((-val, l, n - 1))
            
        heapq.heapify(pq)
        
        # 3. Extract top k elements
        total_value = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(pq)
            total_value += -neg_val
            
            # Push the next interval (l, r-1) if valid
            if r > l:
                next_val = get_val(l, r - 1)
                heapq.heappush(pq, (-next_val, l, r - 1))
                
        return total_value