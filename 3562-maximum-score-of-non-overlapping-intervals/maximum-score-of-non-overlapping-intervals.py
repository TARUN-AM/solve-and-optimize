from bisect import bisect_left
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Store: right endpoint, left endpoint, weight, original index
        jobs = [
            (right, left, weight, index)
            for index, (left, right, weight) in enumerate(intervals)
        ]

        # Sort by ending position
        jobs.sort()

        n = len(jobs)
        ends = [job[0] for job in jobs]

        # dp[count][i] = best result using the first i sorted intervals
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        def better(first, second):
            """
            Return the better result between two (score, indices) pairs.
            """
            score1, indices1 = first
            score2, indices2 = second

            if score1 != score2:
                return first if score1 > score2 else second

            return first if indices1 < indices2 else second

        for i in range(1, n + 1):
            right, left, weight, original_index = jobs[i - 1]

            # The compatible prefix contains intervals ending before `left`.
            previous_count = bisect_left(ends, left, 0, i - 1)

            for count in range(1, 5):
                # Option 1: skip the current interval
                skip = dp[count][i - 1]

                # Option 2: take the current interval
                previous_score, previous_indices = dp[count - 1][previous_count]

                take = (
                    previous_score + weight,
                    sorted(previous_indices + [original_index])
                )

                dp[count][i] = better(skip, take)

        # Compare answers using at most 4 intervals
        answer = (0, [])

        for count in range(1, 5):
            answer = better(answer, dp[count][n])

        return answer[1]