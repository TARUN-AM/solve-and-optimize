class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for value in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(value)
            else:
                arr2.append(value)

        return arr1 + arr2