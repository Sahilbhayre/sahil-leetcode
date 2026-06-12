class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        # Precompute powers of 2 (O(1) lookup later)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # FAST BFS: Using a list iteration is faster than deque in Python
        visited = [False] * (n + 1)
        q = [1]
        visited[1] = True
        up[1][0] = 1
        
        for u in q:
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    q.append(v)
                    
        # Build the Binary Lifting Table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Process Queries with INLINED LCA (Removes function call overhead!)
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            orig_u, orig_v = u, v
            
            # --- START INLINED LCA ---
            if depth[u] < depth[v]:
                u, v = v, u
                
            diff = depth[u] - depth[v]
            j = 0
            while diff > 0:
                if diff & 1:
                    u = up[u][j]
                diff >>= 1
                j += 1
                
            if u == v:
                lca = u
            else:
                for j in range(LOG - 1, -1, -1):
                    if up[u][j] != up[v][j]:
                        u = up[u][j]
                        v = up[v][j]
                lca = up[u][0]
            # --- END INLINED LCA ---
            
            k = depth[orig_u] + depth[orig_v] - 2 * depth[lca]
            ans.append(pow2[k - 1])
            
        return ans