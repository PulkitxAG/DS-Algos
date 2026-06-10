class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        t=2
        for i in range(1,n+1):
            if t*2==i:
                dp[i]=1
                t=i
            else:
                dp[i]=dp[i-t]+1
        return dp