import heapq
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(
        self,
        lists: list[Optional["ListNode"]]
    ) -> Optional["ListNode"]:
        heap = []

        # Add the first node of every non-empty list.
        for list_index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(
                    heap,
                    (node.val, list_index, node)
                )

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, list_index, node = heapq.heappop(heap)

            tail.next = node
            tail = node

            if node.next is not None:
                heapq.heappush(
                    heap,
                    (node.next.val, list_index, node.next)
                )

        # Ensure the merged list terminates correctly.
        tail.next = None

        return dummy.next