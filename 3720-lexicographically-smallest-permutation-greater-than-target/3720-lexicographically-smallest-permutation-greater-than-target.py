class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        # Try changing position i, from right to left.
        for i in range(n - 1, -1, -1):

            # Count all characters in s
            count = [0] * 26
            for ch in s:
                count[ord(ch) - 97] += 1

            # Use target[0:i] as the prefix.
            possible = True

            for j in range(i):
                x = ord(target[j]) - 97

                if count[x] == 0:
                    possible = False
                    break

                count[x] -= 1

            if not possible:
                continue

            # At position i, find the smallest character
            # that is greater than target[i].
            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if count[c] > 0:
                    result = target[:i] + chr(c + 97)
                    count[c] -= 1

                    # Fill remaining positions with smallest chars
                    for j in range(26):
                        result += chr(j + 97) * count[j]

                    return result

        return ""