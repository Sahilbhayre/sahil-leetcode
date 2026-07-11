class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :type rtype: int
        """
        adj = {i: [] for i in range(n)}
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        visited = set()
        complete_components_count = 0

        for i in range(n):
            if i not in visited:
                component_nodes = []
                stack = [i]
                visited.add(i)
                
                while stack:
                    curr = stack.pop()
                    component_nodes.append(curr)
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                
            
                total_nodes = len(component_nodes)
                is_complete = True
                
                for node in component_nodes:
                    if degree[node] != total_nodes - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count