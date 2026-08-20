class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        reversed_s = s[::-1]
        combined = s + "#" + reversed_s

        # lps[i] = length of the longest proper prefix of combined
        # that is also a suffix ending at index i.
        lps = [0] * len(combined)

        j = 0

        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        longest_palindromic_prefix = lps[-1]

        # Add the reverse of the non-palindromic suffix to the front.
        return (
            reversed_s[:len(s) - longest_palindromic_prefix]
            + s
        )