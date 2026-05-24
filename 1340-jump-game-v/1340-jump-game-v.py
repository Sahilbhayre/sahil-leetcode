class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            max_visited = 1 #Base Case

            #1. Jumping to the right(i+x)
            for x in range(1, d+1):
                j = i + x
                if j>=n or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))

            #2. Jumping to left (i-x)
            for x in range(1, d+1):
                j = i-x
                if j<0 or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))

            memo[i] = max_visited
            return max_visited
        
        return max(dfs(i) for i in range(n))