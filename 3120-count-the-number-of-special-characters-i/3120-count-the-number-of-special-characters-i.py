class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_set = set()
        upper_set = set()

        for char in word:
            if char.islower():
                lower_set.add(char)
            else:
                upper_set.add(char)

        special_count = 0
        for char in lower_set:
            if char.upper() in upper_set:
                special_count += 1

        return special_count