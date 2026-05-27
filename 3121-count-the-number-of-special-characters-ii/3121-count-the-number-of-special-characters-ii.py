class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        char_status = [-1] * 26
        
        for ch in word:
            if ch.islower():
                idx = ord(ch) - ord('a')
                if char_status[idx] == -1 or char_status[idx] == 0:
                    char_status[idx] = 0  # Valid lowercase state
                elif char_status[idx] == 1 or char_status[idx] == 2:
                    char_status[idx] = 2  # Lowercase after uppercase -> Invalid
            else:
                idx = ord(ch) - ord('A')
                if char_status[idx] == 0:
                    char_status[idx] = 1  # First uppercase after lowercase -> Valid candidate
                elif char_status[idx] == -1:
                    char_status[idx] = 2  # Uppercase before lowercase -> Invalid
                    
        # Count how many characters successfully reached state 1
        return char_status.count(1)