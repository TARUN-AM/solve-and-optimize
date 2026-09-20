class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0

        for position, character in enumerate(s, start=1):
            reverse_value = 26 - (ord(character) - ord('a'))
            answer += position * reverse_value

        return answer