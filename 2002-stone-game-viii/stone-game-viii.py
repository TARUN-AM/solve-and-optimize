class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        total = 0

        for stone in stones:
            total += stone

        best = total

        for i in range(len(stones) - 2, 0, -1):
            total -= stones[i + 1]
            best = max(best, total - best)

        return best