class Solution:
    def isPalindrome(self, x):
        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Numbers ending in 0 are not palindromes,
        # except 0 itself
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even number of digits
        # Example: 1221 -> x = 12, reversed_half = 12
        #
        # Odd number of digits
        # Example: 121 -> x = 12, reversed_half = 121
        # Remove the middle digit using // 10
        return x == reversed_half or x == reversed_half // 10