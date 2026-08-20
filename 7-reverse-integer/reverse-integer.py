class Solution:
    def reverse(self, x: int) -> int:
        minimum = -(2 ** 31)
        maximum = 2 ** 31 - 1

        result = 0

        while x != 0:
            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10

            if result < minimum // 10 + 1 or result > maximum // 10:
                return 0

            result = result * 10 + digit

        return result
        