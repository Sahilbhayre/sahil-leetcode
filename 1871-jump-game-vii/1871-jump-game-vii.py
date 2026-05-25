class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[n-1] == '1':
            return False

        dp = [False] * n
        dp[0] = True

        reachable_count = 0

        for i in range(1,n):
            ## 2. Remove the oldest element exiting the window on the right
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
                    
            # 2. Remove the oldest element exiting the window on the left
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # 3. If s[i] is '0' and we have at least one reachable index in our window
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]