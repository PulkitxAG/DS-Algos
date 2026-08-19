class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        count = 0 
        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triplet_sum = arr[i] + arr[j] + arr[k]
                    if l <= triplet_sum <= r:
                        count += 1
        return count
