class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()

        def count(x):
            ans = 0

            for i in range(len(arr) - 2):
                left = i + 1
                right = len(arr) - 1

                while left < right:
                    if arr[i] + arr[left] + arr[right] <= x:
                        ans += right - left
                        left += 1
                    else:
                        right -= 1

            return ans

        return count(r) - count(l - 1)