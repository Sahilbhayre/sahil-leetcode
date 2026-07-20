class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        res = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                new_idx = (r * n + c + k) % total
                res[new_idx // n][new_idx % n] = grid[r][c]
            
        return res