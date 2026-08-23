class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(value: int) -> int:
            left = 0
            right = len(nums)

            while left < right:
                middle = (left + right) // 2

                if nums[middle] < value:
                    left = middle + 1
                else:
                    right = middle

            return left

        start = lower_bound(target)

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = lower_bound(target + 1) - 1

        return [start, end]