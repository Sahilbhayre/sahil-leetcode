class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []

        for word in words:
            word_weight = 0
            for char in word:
                index = ord(char) - ord('a')
                word_weight += weights[index]

            mod_val = word_weight % 26
            mapped_char = chr(ord('z') - mod_val)
            result.append(mapped_char)

        return "".join(result)