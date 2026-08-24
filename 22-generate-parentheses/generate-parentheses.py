class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        current = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == n and close_count == n:
                result.append("".join(current))
                return

            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count)
                current.pop()

            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1)
                current.pop()

        backtrack(0, 0)
        return result