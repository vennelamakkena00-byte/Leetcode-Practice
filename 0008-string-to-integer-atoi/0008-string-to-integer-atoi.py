class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Read digits
        result = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        # 4. Apply sign
        result *= sign

        # 5. Clamp to 32-bit signed integer range
        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result