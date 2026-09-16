class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        numerator = 1
        denominator = 1

        r = 2 * k
        total = n + k - 1

        for i in range(r):
            numerator = numerator * (total - i) % MOD
            denominator = denominator * (i + 1) % MOD

        inverse_denominator = pow(denominator, MOD - 2, MOD)

        return numerator * inverse_denominator % MOD