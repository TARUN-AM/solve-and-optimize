class Solution:
    def permute(self, nums):
        result = []
        used = [False] * len(nums)
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                current.append(nums[i])

                backtrack()

                current.pop()
                used[i] = False

        backtrack()
        return result