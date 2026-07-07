class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        x = 0
        digit_sum = 0
        prod = 1

        while n > 0:
            digit = n % 10
            if digit != 0:
                digit_sum += digit
                x += digit * prod
                prod *= 10

            n //= 10
        
        return x * digit_sum