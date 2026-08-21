class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        used = [False] * n
        current = []

        def backtrack() -> None:
            if len(current) == n:
                result.append(current.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return result