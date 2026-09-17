from typing import List


class Solution:
    def minSumOfLengths(
        self,
        arr: List[int],
        target: int
    ) -> int:
        n = len(arr)
        INF = n + 1

        # best[i] = shortest target-sum subarray completely
        # contained in arr[0:i]
        best = [INF] * (n + 1)

        answer = INF
        prefix_sum = 0

        # Stores the latest index for every prefix sum
        first_index = {0: 0}

        for i, value in enumerate(arr, start=1):
            prefix_sum += value

            # Carry forward the best previous subarray
            best[i] = best[i - 1]

            previous_prefix = prefix_sum - target

            if previous_prefix in first_index:
                start = first_index[previous_prefix]
                current_length = i - start

                # The previous best must end before this subarray starts
                answer = min(
                    answer,
                    best[start] + current_length
                )

                # Update the shortest subarray ending at i
                best[i] = min(best[i], current_length)

            # Store the earliest occurrence of this prefix sum
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

        return -1 if answer == INF else answer