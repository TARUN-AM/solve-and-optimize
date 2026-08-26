class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1] * (n + 1)

        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        numbers = list(range(1, n + 1))
        k -= 1
        result = []

        for remaining in range(n, 0, -1):
            block_size = factorial[remaining - 1]
            index, k = divmod(k, block_size)

            result.append(str(numbers.pop(index)))

        return "".join(result)