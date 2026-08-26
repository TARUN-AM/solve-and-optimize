class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right, char in enumerate(s):
            if char == "1":
                ones += 1

            while ones == k:
                current = s[left:right + 1]

                if not best or len(current) < len(best):
                    best = current
                elif len(current) == len(best) and current < best:
                    best = current

                if s[left] == "1":
                    ones -= 1

                left += 1

        return best