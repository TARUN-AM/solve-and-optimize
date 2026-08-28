class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        lps = [0] * m

        length = 0
        i = 1

        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1

        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - m
            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return -1