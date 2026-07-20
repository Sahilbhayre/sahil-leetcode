class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        ans = 0

        for i, char in enumerate(s):
            last_seen[char] = i
            ans += 1 + min(last_seen['a'], last_seen['b'], last_seen['c'])

        return ans