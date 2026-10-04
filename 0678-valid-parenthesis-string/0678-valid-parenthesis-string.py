class Solution(object):
    def checkValidString(self, s):
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Too many ')' even if '*' are used as '('
            if high < 0:
                return False

            # low cannot be negative
            low = max(0, low)

        # Valid only if we can have exactly 0 unmatched '('
        return low == 0