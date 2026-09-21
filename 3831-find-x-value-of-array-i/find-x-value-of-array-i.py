from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * k

        # previous[r] =
        # number of subarrays ending at the previous index
        # whose product % k equals r
        previous = [0] * k

        for num in nums:
            value = num % k
            current = [0] * k

            # Start a new subarray containing only num
            current[value] += 1

            # Extend every subarray ending at the previous index
            for remainder in range(k):
                new_remainder = (remainder * value) % k
                current[new_remainder] += previous[remainder]

            # Add subarrays ending at this index to the final answer
            for remainder in range(k):
                answer[remainder] += current[remainder]

            previous = current

        return answer