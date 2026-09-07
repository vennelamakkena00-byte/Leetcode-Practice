class Solution:
    def distinctSubseqII(self, s):
        MOD = 1000000007
        n = len(s)

        dp = 1
        last = [0] * 26

        for ch in s:
            c = ord(ch) - ord('a')

            new_dp = (2 * dp - last[c]) % MOD

            last[c] = dp
            dp = new_dp

        return (dp - 1) % MOD