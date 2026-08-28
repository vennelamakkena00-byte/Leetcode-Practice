class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check palindrome possibility
        odd_char = -1

        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd_char != -1:
                    return ""
                odd_char = i

        # Counts for the left half
        half = [x // 2 for x in cnt]
        m = n // 2

        def build(left):
            if n % 2 == 1:
                return left + chr(odd_char + 97) + left[::-1]
            return left + left[::-1]

        # -------------------------------------------------
        # Case 1: Can we make target's left half exactly?
        # -------------------------------------------------

        target_left = target[:m]

        remaining = half[:]
        possible = True

        for ch in target_left:
            x = ord(ch) - 97

            if remaining[x] == 0:
                possible = False
                break

            remaining[x] -= 1

        if possible:
            candidate = build(target_left)

            # Exact left half, but palindrome itself must be greater
            if candidate > target:
                return candidate

        # -------------------------------------------------
        # Case 2:
        # Find the smallest left half strictly greater
        # than target_left.
        # -------------------------------------------------

        # We try every possible pivot from right to left.
        #
        # Positions before pivot must exactly match target.
        # At pivot, choose the smallest available character
        # greater than target[pivot].
        # Everything after pivot is filled minimally.

        for pivot in range(m - 1, -1, -1):

            remaining = half[:]

            # Match target characters before pivot
            possible = True

            for j in range(pivot):
                x = ord(target_left[j]) - 97

                if remaining[x] == 0:
                    possible = False
                    break

                remaining[x] -= 1

            if not possible:
                continue

            current = ord(target_left[pivot]) - 97

            # Try the smallest character greater than target[pivot]
            for c in range(current + 1, 26):

                if remaining[c] == 0:
                    continue

                remaining[c] -= 1

                # Build the smallest possible suffix
                suffix = []

                for x in range(26):
                    if remaining[x] > 0:
                        suffix.extend(
                            [chr(x + 97)] * remaining[x]
                        )

                left = target_left[:pivot] + chr(c + 97) + "".join(suffix)

                candidate = build(left)

                if candidate > target:
                    return candidate

                remaining[c] += 1

        return ""