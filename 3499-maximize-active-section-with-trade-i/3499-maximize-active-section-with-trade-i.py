class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = '1' + s + '1'\

        blocks = []
        i = 0
        n = len(t)
        
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
            
        initial_ones = s.count('1')
        max_gain = 0
        
        for k in range(1, len(blocks) - 1):
            if blocks[k][0] == '1':
                if blocks[k - 1][0] == '0' and blocks[k + 1][0] == '0':
                    z1 = blocks[k - 1][1]
                    z2 = blocks[k + 1][1]
                    max_gain = max(max_gain, z1 + z2)
                    
        return initial_ones + max_gain