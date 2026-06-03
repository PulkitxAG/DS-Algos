class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1000000007

        req = [-1] * n
        mx = 0

        for end, cnt in requirements:
            req[end] = cnt
            mx = max(mx, cnt)

        if req[0] > 0:
            return 0

        req[0] = 0

        dp = [0] * (mx + 1)
        dp[0] = 1

        for i in range(1, n):
            pref = [0] * (mx + 2)

            for j in range(mx + 1):
                pref[j + 1] = (pref[j] + dp[j]) % MOD

            ndp = [0] * (mx + 1)

            if req[i] != -1:
                j = req[i]
                l = max(0, j - i)
                ndp[j] = (pref[j + 1] - pref[l]) % MOD
            else:
                for j in range(mx + 1):
                    l = max(0, j - i)
                    ndp[j] = (pref[j + 1] - pref[l]) % MOD

            dp = ndp

        return dp[req[n - 1]]