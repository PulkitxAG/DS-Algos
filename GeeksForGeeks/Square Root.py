class Solution:
    def floorSqrt(self, n):
        start = 0
        end = n
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid <= n:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans