from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            index = ord(ch) - ord('a')
            first[index] = min(first[index], i)
            last[index] = i

        candidates = []

        def build_interval(start: int):
            end = last[ord(s[start]) - ord('a')]
            i = start

            while i <= end:
                current = ord(s[i]) - ord('a')

                # This character starts before the current interval,
                # so the interval cannot be valid.
                if first[current] < start:
                    return None

                end = max(end, last[current])
                i += 1

            return start, end

        # Build valid candidate intervals
        for start in range(n):
            current = ord(s[start]) - ord('a')

            # Only begin from the first occurrence of a character
            if first[current] != start:
                continue

            interval = build_interval(start)

            if interval is not None:
                candidates.append(interval)

        # Select maximum number of non-overlapping intervals.
        # Sorting by ending position gives the greedy strategy.
        candidates.sort(key=lambda interval: interval[1])

        answer = []
        previous_end = -1

        for start, end in candidates:
            if start > previous_end:
                answer.append(s[start:end + 1])
                previous_end = end

        return answer