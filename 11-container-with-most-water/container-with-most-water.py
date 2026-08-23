class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            maximum_area = max(maximum_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum_area