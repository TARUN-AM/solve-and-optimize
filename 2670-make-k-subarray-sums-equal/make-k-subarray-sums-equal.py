class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        from math import gcd
from statistics import median

class Solution:
    def makeSubKSumEqual(self, arr, k):
        n = len(arr)

        g = gcd(n, k)

        visited = [False] * n
        operations = 0

        for i in range(g):

            group = []
            j = i

            while not visited[j]:
                visited[j] = True
                group.append(arr[j])

                j = (j + k) % n

            group.sort()

            target = group[len(group) // 2]

            for num in group:
                operations += abs(num - target)

        return operations