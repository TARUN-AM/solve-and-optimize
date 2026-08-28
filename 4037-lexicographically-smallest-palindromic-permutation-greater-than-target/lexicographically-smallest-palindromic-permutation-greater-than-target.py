class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_length = n // 2
        counts = [0] * 26

        for char in s:
            counts[ord(char) - 97] += 1

        odd_count = 0
        middle = ""

        for i, count in enumerate(counts):
            if count % 2:
                odd_count += 1
                middle = chr(i + 97)

        if odd_count > n % 2:
            return ""

        half_counts = [count // 2 for count in counts]
        calendrix = s

        def make_palindrome(left_half: str) -> str:
            return left_half + middle + left_half[::-1]

        candidates = []

        remaining = half_counts[:]
        exact_half = []
        possible = True

        for char in target[:half_length]:
            index = ord(char) - 97

            if remaining[index] == 0:
                possible = False
                break

            remaining[index] -= 1
            exact_half.append(char)

        if possible:
            palindrome = make_palindrome("".join(exact_half))

            if palindrome > target:
                candidates.append(palindrome)

        remaining = half_counts[:]
        pivot = -1

        for i, char in enumerate(target[:half_length]):
            index = ord(char) - 97

            for greater in range(index + 1, 26):
                if remaining[greater]:
                    pivot = i

            if remaining[index] == 0:
                break

            remaining[index] -= 1

        if pivot != -1:
            remaining = half_counts[:]

            for char in target[:pivot]:
                remaining[ord(char) - 97] -= 1

            index = ord(target[pivot]) - 97 + 1

            while index < 26 and remaining[index] == 0:
                index += 1

            if index < 26:
                remaining[index] -= 1

                left_half = (
                    target[:pivot]
                    + chr(index + 97)
                    + "".join(
                        chr(i + 97) * remaining[i]
                        for i in range(26)
                    )
                )

                candidates.append(make_palindrome(left_half))

        return min(candidates) if candidates else ""