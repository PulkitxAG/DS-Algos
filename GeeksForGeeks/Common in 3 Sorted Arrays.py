class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        ans = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):

            if arr1[i] == arr2[j] == arr3[k]:
                if not ans or ans[-1] != arr1[i]:
                    ans.append(arr1[i])

                i += 1
                j += 1
                k += 1

            elif arr1[i] < arr2[j]:
                i += 1

            elif arr2[j] < arr3[k]:
                j += 1

            else:
                k += 1

        return ans