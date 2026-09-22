from typing import List


class Node:
    __slots__ = ("product", "count")

    def __init__(self, product: int = 1, count=None):
        self.product = product
        self.count = count if count is not None else []


class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [
            Node(1, [0] * k)
            for _ in range(4 * self.n)
        ]

        self.build(1, 0, self.n - 1, nums)

    def merge(self, left: Node, right: Node) -> Node:
        product = (left.product * right.product) % self.k
        count = [0] * self.k

        # Prefixes that end inside the left child
        for remainder in range(self.k):
            count[remainder] += left.count[remainder]

        # Prefixes that use all of the left child
        # and continue into the right child
        for remainder in range(self.k):
            shifted = (left.product * remainder) % self.k
            count[shifted] += right.count[remainder]

        return Node(product, count)

    def build(
        self,
        node: int,
        left: int,
        right: int,
        nums: List[int]
    ) -> None:
        if left == right:
            value = nums[left] % self.k
            count = [0] * self.k
            count[value] = 1

            self.tree[node] = Node(value, count)
            return

        middle = (left + right) // 2

        self.build(node * 2, left, middle, nums)
        self.build(node * 2 + 1, middle + 1, right, nums)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(
        self,
        node: int,
        left: int,
        right: int,
        index: int,
        value: int
    ) -> None:
        if left == right:
            value %= self.k
            count = [0] * self.k
            count[value] = 1

            self.tree[node] = Node(value, count)
            return

        middle = (left + right) // 2

        if index <= middle:
            self.update(node * 2, left, middle, index, value)
        else:
            self.update(node * 2 + 1, middle + 1, right, index, value)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(
        self,
        node: int,
        left: int,
        right: int,
        query_left: int,
        query_right: int
    ) -> Node | None:
        if query_left <= left and right <= query_right:
            return self.tree[node]

        middle = (left + right) // 2

        if query_right <= middle:
            return self.query(
                node * 2,
                left,
                middle,
                query_left,
                query_right
            )

        if query_left > middle:
            return self.query(
                node * 2 + 1,
                middle + 1,
                right,
                query_left,
                query_right
            )

        left_result = self.query(
            node * 2,
            left,
            middle,
            query_left,
            query_right
        )

        right_result = self.query(
            node * 2 + 1,
            middle + 1,
            right,
            query_left,
            query_right
        )

        return self.merge(left_result, right_result)


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:
        segment_tree = SegmentTree(nums, k)
        answer = []

        n = len(nums)

        for index, value, start, x in queries:
            # The update persists for all future queries
            segment_tree.update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query the range nums[start:]
            result = segment_tree.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            answer.append(result.count[x])

        return answer