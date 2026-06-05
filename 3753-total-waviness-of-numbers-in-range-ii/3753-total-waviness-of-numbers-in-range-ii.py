class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :type rtype: int
        """
        
        def solve(num_str):
            if not num_str:
                return 0
            
            n = len(num_str)
            memo = {} # Manual memoization table for Python 2
            
            def dp(idx, tight, leading, last, second_last):
                # Create a unique state key for caching
                state = (idx, tight, leading, last, second_last)
                if state in memo:
                    return memo[state]
                
                if idx == n:
                    return 1, 0
                
                limit = int(num_str[idx]) if tight else 9
                total_count = 0
                total_wave = 0
                
                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    
                    if leading and d == 0:
                        count, wave = dp(idx + 1, next_tight, True, -1, -1)
                        total_count += count
                        total_wave += wave
                    else:
                        is_wave = 0
                        if not leading and last != -1 and second_last != -1:
                            if second_last < last > d:    # Peak
                                is_wave = 1
                            elif second_last > last < d:  # Valley
                                is_wave = 1
                        
                        count, wave = dp(idx + 1, next_tight, False, d, last)
                        total_count += count
                        total_wave += (is_wave * count) + wave
                
                memo[state] = (total_count, total_wave)
                return memo[state]

            return dp(0, True, True, -1, -1)[1]

        return solve(str(num2)) - solve(str(num1 - 1))