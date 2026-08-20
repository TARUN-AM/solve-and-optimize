class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], index]

            seen[value] = index

        # The problem guarantees exactly one valid answer.
        return []