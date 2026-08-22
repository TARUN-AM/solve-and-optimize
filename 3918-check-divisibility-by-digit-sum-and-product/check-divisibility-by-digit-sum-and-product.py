class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        value = n

        while value:
            digit = value % 10
            digit_sum += digit
            digit_product *= digit
            value //= 10

        return n % (digit_sum + digit_product) == 0