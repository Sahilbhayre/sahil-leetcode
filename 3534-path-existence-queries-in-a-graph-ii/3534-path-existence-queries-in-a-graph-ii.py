class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        sorted_nodes = sorted(range(n), key=lambda x: nums[x])
        
        
        rank = [0] * n
        for r, idx in enumerate(sorted_nodes):
            rank[idx] = r
            
        
        LOG = 17  
        up = [[-1] * LOG for _ in range(n)]
        
        right = 0
        for left in range(n):
            while right < n and nums[sorted_nodes[right]] - nums[sorted_nodes[left]] <= maxDiff:
                right += 1
            
            up[left][0] = right - 1
            
        for j in range(1, LOG):
            for i in range(n):
                parent = up[i][j - 1]
                if parent != -1:
                    up[i][j] = up[parent][j - 1]
                else:
                    up[i][j] = -1
                    
      
        def get_distance(u, v):
            if u == v:
                return 0
            if u > v:
                u, v = v, u  
                
            ans = 0
            curr = u
            
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] != -1 and up[curr][j] < v:
                    curr = up[curr][j]
                    ans += (1 << j)
                    
            if up[curr][0] >= v:
                return ans + 1
                
            return -1

        result = []
        for u, v in queries:
            result.append(get_distance(rank[u], rank[v]))
            
        return result