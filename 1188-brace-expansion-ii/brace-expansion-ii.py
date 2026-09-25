from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # Each stack item stores:
        # (outer_current, outer_union)
        stack = []

        current = {""}
        union = set()

        for character in expression:
            if character.isalpha():
                # Concatenate this letter to every current word
                current = {
                    word + character
                    for word in current
                }

            elif character == "{":
                # Save the state outside this brace level
                stack.append((current, union))

                # Start parsing the expression inside braces
                current = {""}
                union = set()

            elif character == ",":
                # Finish the current comma-separated alternative
                union.update(current)

                # Start a new alternative
                current = {""}

            else:  # character == "}"
                # Include the final alternative before closing
                union.update(current)

                inside = union
                outer_current, outer_union = stack.pop()

                # Concatenate the brace result with the expression before it
                current = {
                    left + right
                    for left in outer_current
                    for right in inside
                }

                # Restore the union belonging to the outer level
                union = outer_union

        # The final alternative may not have been followed by '}'
        union.update(current)

        return sorted(union)