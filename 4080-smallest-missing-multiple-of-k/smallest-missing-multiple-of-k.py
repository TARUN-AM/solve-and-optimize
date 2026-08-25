class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        values = set(nums)
        multiple = k

        while multiple in values:
            multiple += k

        return multiple