class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[r][c] will store [max_score, num_paths]
        # Initialize with [-1, 0] to represent unreachable states
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Starting at 'E' (0, 0)
        dp[0][0] = [0, 1]
        
        # Iterate through the board
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'X' or dp[r][c][0] == -1:
                    continue
                    
                current_score, current_paths = dp[r][c]
                
                # Try moving to 3 possible directions: Down, Right, Diagonal Down-Right
                directions = [(r + 1, c), (r, c + 1), (r + 1, c + 1)]
                
                for nr, nc in directions:
                    if nr < n and nc < n and board[nr][nc] != 'X':
                        # Determine the value of the next cell
                        cell_value = 0
                        if board[nr][nc].isdigit():
                            cell_value = int(board[nr][nc])
                        
                        next_score = current_score + cell_value
                        
                        # If we found a strictly better path to (nr, nc)
                        if next_score > dp[nr][nc][0]:
                            dp[nr][nc][0] = next_score
                            dp[nr][nc][1] = current_paths
                        # If we found an alternative path with the exact same max score
                        elif next_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + current_paths) % MOD
        
        # Destination is 'S' at (n-1, n-1)
        max_score, paths = dp[n-1][n-1]
        
        return [max_score, paths] if max_score != -1 else [0, 0]