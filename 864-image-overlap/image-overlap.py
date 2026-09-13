from collections import Counter
from typing import List


class Solution:
    def largestOverlap(
        self,
        img1: List[List[int]],
        img2: List[List[int]]
    ) -> int:
        ones1 = []
        ones2 = []

        n = len(img1)

        # Store coordinates of all 1s in img1
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))

        # Store coordinates of all 1s in img2
        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    ones2.append((r, c))

        shifts = Counter()

        # Count translation required for every pair of 1s
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] += 1

        return max(shifts.values(), default=0)