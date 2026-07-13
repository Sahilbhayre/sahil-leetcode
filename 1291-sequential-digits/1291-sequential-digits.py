class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        sample = '123456789'
        result = []

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):
            for i in range(10 - length):
                substring = sample[i: i + length]
                num = int(substring)

                if low <= num <= high:
                    result.append(num)

        return result