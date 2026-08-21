class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        n = len(s)
        i = 0

      
        while i < n and s[i] == " ":
            i += 1

        
        sign = 1

        if i < n:
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1

        result = 0

        
        while i < n:
            digit = ord(s[i]) - ord("0")

            if digit < 0 or digit > 9:
                break

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        result *= sign

        return max(INT_MIN, min(INT_MAX, result))