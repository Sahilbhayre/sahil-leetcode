from collections import deque, defaultdict

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        # Step 2: BFS to find the minimum edge in the connected component
        min_score = float('inf')
        queue = deque([1])
        visited = {1}
        
        while queue:
            node = queue.popleft()
            
            for neighbor, weight in graph[node]:
                # Track the minimum weight seen anywhere in this component
                min_score = min(min_score, weight)
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score