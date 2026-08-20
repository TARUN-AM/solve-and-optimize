class Solution:
    def findAnswer(self, parent: list[int], s: str) -> list[bool]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[parent[node]].append(node)

        traversal = []
        start = [0] * n
        finish = [0] * n

        stack = [(0, 0)]

        while stack:
            node, state = stack.pop()

            if state == 0:
                start[node] = len(traversal)
                stack.append((node, 1))

                for child in reversed(children[node]):
                    stack.append((child, 0))
            else:
                traversal.append(s[node])
                finish[node] = len(traversal)

        text = "#" + "#".join(traversal) + "#"
        radius = [0] * len(text)

        center = 0
        right = 0

        for i in range(len(text)):
            mirror = 2 * center - i

            if i < right:
                radius[i] = min(right - i, radius[mirror])

            left = i - radius[i] - 1
            current_right = i + radius[i] + 1

            while (
                left >= 0
                and current_right < len(text)
                and text[left] == text[current_right]
            ):
                radius[i] += 1
                left -= 1
                current_right += 1

            if i + radius[i] > right:
                center = i
                right = i + radius[i]

        answer = [False] * n

        for node in range(n):
            left = start[node]
            length = finish[node] - start[node]

            center_index = 2 * left + length

            answer[node] = radius[center_index] >= length

        return answer