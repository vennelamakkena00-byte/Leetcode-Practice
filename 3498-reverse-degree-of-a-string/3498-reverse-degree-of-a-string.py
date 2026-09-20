class Solution(object):
    def reverseDegree(self, s):
        total = 0

        for i in range(len(s)):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reverse_value = ord('z') - ord(s[i]) + 1

            # i + 1 because position is 1-indexed
            total += reverse_value * (i + 1)

        return total