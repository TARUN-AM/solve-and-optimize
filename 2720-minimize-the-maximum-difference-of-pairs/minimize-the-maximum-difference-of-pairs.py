class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def can_form_pairs(max_difference: int) -> bool:
            pairs = 0
            i = 0
            n = len(nums)

            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_difference:
                    pairs += 1
                    i += 2

                    if pairs == p:
                        return True
                else:
                    i += 1

            return False

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            middle = (left + right) // 2

            if can_form_pairs(middle):
                right = middle
            else:
                left = middle + 1

        return left