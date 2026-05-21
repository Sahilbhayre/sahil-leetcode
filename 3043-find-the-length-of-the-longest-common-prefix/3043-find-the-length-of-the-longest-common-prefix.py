class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()

        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10
            
        max_length = 0

        for val in arr2:
            while val > 0:
                if val in prefixes:
                    max_length = max(max_length, len(str(val)))
                    break
                val //= 10

        return max_length