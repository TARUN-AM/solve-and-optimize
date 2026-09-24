from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index, number in enumerate(nums):
            digit_sum = sum(int(digit) for digit in str(number))

            if digit_sum == index:
                return index

        return -1