class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # We need C(n + k - 1, 2k)
        N = n + k - 1
        R = 2 * k

        # factorials
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # modular inverse using Fermat's little theorem
        def modpow(a, b):
            result = 1
            while b:
                if b & 1:
                    result = result * a % MOD
                a = a * a % MOD
                b >>= 1
            return result

        inv_fact = [1] * (N + 1)
        inv_fact[N] = modpow(fact[N], MOD - 2)

        for i in range(N, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        return fact[N] * inv_fact[R] % MOD * inv_fact[N - R] % MOD