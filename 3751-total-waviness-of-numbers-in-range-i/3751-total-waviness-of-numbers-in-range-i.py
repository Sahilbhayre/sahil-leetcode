class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total_waviness = 0

        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)

            if n<3:
                continue
            
            for i in range(1, n-1):
                prev_digit = s[i-1]
                curr_digit = s[i]
                next_digit = s[i+1]

                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1

                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
        return total_waviness
        