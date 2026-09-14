from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int, index: int) -> bool:
            # Boundary check or character mismatch
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            # The complete word has been found
            if index == len(word) - 1:
                return True

            # Mark this cell as visited
            original = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1) or  # Down
                dfs(row - 1, col, index + 1) or  # Up
                dfs(row, col + 1, index + 1) or  # Right
                dfs(row, col - 1, index + 1)     # Left
            )

            # Restore the cell for other paths
            board[row][col] = original

            return found

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False