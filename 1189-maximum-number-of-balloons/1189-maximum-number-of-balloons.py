class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2
        o = text.count('o') // 2
        n = text.count('n')

        return min(b, a, l, o, n)