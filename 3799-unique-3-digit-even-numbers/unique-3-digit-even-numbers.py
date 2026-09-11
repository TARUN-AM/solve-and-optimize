from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = [0] * 10

        for digit in digits:
            available[digit] += 1

        answer = 0

        for number in range(100, 1000, 2):
            a = number // 100
            b = (number // 10) % 10
            c = number % 10

            if a == b == c:
                valid = available[a] >= 3
            elif a == b:
                valid = available[a] >= 2 and available[c] >= 1
            elif a == c:
                valid = available[a] >= 2 and available[b] >= 1
            elif b == c:
                valid = available[b] >= 2 and available[a] >= 1
            else:
                valid = (
                    available[a] >= 1
                    and available[b] >= 1
                    and available[c] >= 1
                )

            if valid:
                answer += 1

        return answer