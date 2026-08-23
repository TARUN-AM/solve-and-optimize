from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        @lru_cache(None)
        def dp(i: int, j: int) -> bool:
            if j == m:
                return i == n

            first_match = (
                i < n and
                (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < m and p[j + 1] == "*":
                return (
                    dp(i, j + 2)
                    or (first_match and dp(i + 1, j))
                )

            return first_match and dp(i + 1, j + 1)

        return dp(0, 0)