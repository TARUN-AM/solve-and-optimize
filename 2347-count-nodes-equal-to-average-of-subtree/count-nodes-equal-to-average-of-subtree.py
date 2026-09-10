class Solution:
    def averageOfSubtree(self, root):
        self.answer = 0

        def dfs(node):
            if node is None:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == node.val:
                self.answer += 1

            return subtree_sum, subtree_count

        dfs(root)
        return self.answer