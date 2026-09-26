from typing import List


class Solution:
    def evaluate(
        self,
        s: str,
        knowledge: List[List[str]]
    ) -> str:
        values = {key: value for key, value in knowledge}
        result = []

        i = 0

        while i < len(s):
            if s[i] == '(':
                j = i + 1

                # Find the closing bracket
                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]
                result.append(values.get(key, '?'))

                # Skip the closing bracket
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)