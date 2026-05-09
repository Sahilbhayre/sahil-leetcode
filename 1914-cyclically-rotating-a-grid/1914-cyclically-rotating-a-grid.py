class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        num_layers = min(m,n) // 2

        for layer in range(num_layers):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
           
            #1. Append elements in counter-clockwise order
            elements = []

            # Top row
            for j in range(left, right):
                elements.append(grid[top][j])
            
            # Right Column
            for i in range(top, bottom):
                elements.append(grid[i][right])

            # Bottom row
            for j in range(right, left, -1):
                elements.append(grid[bottom][j])

            # Left Column
            for i in range(bottom, top, -1):
                elements.append(grid[i][left])

            #2. Calculate rotation
            total_elements = len(elements)
            shift = k % total_elements

            rotated = elements[shift:] + elements[:shift]

            #3. Put elements into grid
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid   