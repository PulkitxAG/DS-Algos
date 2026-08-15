class Solution:
    def binarySearch(self, arr, k):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                start = mid + 1
            else:
                end = mid - 1

        return False