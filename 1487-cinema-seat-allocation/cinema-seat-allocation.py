class Solution:
    def maxNumberOfFamilies(
        self,
        n: int,
        reservedSeats: list[list[int]]
    ) -> int:
        reserved = {}

        for row, seat in reservedSeats:
            reserved[row] = reserved.get(row, 0) | (1 << (seat - 1))

        left_block = 0b0000011110
        middle_block = 0b0001111000
        right_block = 0b0111100000

        total = (n - len(reserved)) * 2

        for mask in reserved.values():
            if mask & left_block == 0:
                total += 1

            if mask & right_block == 0:
                total += 1

            if (
                mask & left_block
                and mask & right_block
                and mask & middle_block == 0
            ):
                total += 1

        return total