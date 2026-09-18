class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i in range(n):
            c = ord(s[i]) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find the smallest valid interval starting from each character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character appeared before our left boundary,
                # so we cannot make a valid substring starting here.
                if first[x] < left:
                    valid = False
                    break

                # We must include all occurrences of this character.
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position.
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        # Greedily select the interval that finishes earliest.
        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result