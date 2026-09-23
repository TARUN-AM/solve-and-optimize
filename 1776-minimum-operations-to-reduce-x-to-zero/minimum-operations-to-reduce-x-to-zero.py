from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        # No non-empty middle subarray can have a negative sum
        if target < 0:
            return -1

        n = len(nums)

        # If target is zero, remove every element
        if target == 0:
            return n

        left = 0
        current_sum = 0
        longest = -1

        for right, value in enumerate(nums):
            current_sum += value

            # Shrink the window until its sum is <= target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return n - longest