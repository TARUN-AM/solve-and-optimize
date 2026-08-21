class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        from functools import lru_cache
        from math import isqrt

        nums.sort()
        n = len(nums)

        square_pair = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                total = nums[i] + nums[j]
                root = isqrt(total)

                if root * root == total:
                    square_pair[i][j] = True
                    square_pair[j][i] = True

        @lru_cache(None)
        def dp(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1

            total = 0

            for next_index in range(n):
                if mask & (1 << next_index):
                    continue

                if (
                    next_index > 0
                    and nums[next_index] == nums[next_index - 1]
                    and not (mask & (1 << (next_index - 1)))
                ):
                    continue

                if last == -1 or square_pair[last][next_index]:
                    total += dp(
                        mask | (1 << next_index),
                        next_index
                    )

            return total

        return dp(0, -1)