class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def manacher(text: str) -> list[int]:
            radius = [0] * n
            left = 0
            right = -1

            for center in range(n):
                if center > right:
                    current_radius = 1
                else:
                    mirror = left + right - center
                    current_radius = min(
                        radius[mirror],
                        right - center + 1
                    )

                while (
                    center - current_radius >= 0
                    and center + current_radius < n
                    and text[center - current_radius]
                    == text[center + current_radius]
                ):
                    current_radius += 1

                radius[center] = current_radius

                palindrome_right = center + current_radius - 1

                if palindrome_right > right:
                    left = center - current_radius + 1
                    right = palindrome_right

            return radius

        def longest_in_prefix(text: str) -> list[int]:
            radius = manacher(text)

            # best[i] = longest odd palindrome ending exactly at i
            best = [1] * n

            # For a center c with radius r:
            # every ending position e in [c, c + r - 1]
            # has a palindrome of length 2 * (e - c) + 1.
            #
            # We need the active palindrome with the smallest center.
            # That gives the greatest length for the current ending position.
            events = [[] for _ in range(n)]

            for center, r in enumerate(radius):
                palindrome_end = center + r - 1
                events[center].append(palindrome_end)

            active = []
            import heapq

            for end in range(n):
                for palindrome_end in events[end]:
                    heapq.heappush(
                        active,
                        (end, palindrome_end)
                    )

                while active and active[0][1] < end:
                    heapq.heappop(active)

                if active:
                    center = active[0][0]
                    best[end] = 2 * (end - center) + 1

            # Convert exact-ending values to prefix maximums.
            for i in range(1, n):
                best[i] = max(best[i], best[i - 1])

            return best

        left_best = longest_in_prefix(s)

        # Prefixes of reversed(s) correspond to suffixes of s.
        right_best = longest_in_prefix(s[::-1])[::-1]

        answer = 0

        for split in range(1, n):
            answer = max(
                answer,
                left_best[split - 1] * right_best[split]
            )

        return answer