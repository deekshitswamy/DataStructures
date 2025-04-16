import io
from typing import List
from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res, index, arr = 0, [0] * len(nums1), SortedList()
        for i,n in enumerate (nums1):   index[n] = i
        for i,n in enumerate (nums2):   nums1[i] = index[n]
        for i,n in enumerate (reversed(nums1)):
            x = arr.bisect(n) ; arr.add(n) ; res += (i-x)*(n-x)
        return res

obj = Solution()
#data = obj.goodTriplets(n = 1)
#data = obj.goodTriplets(n = 2)
data = obj.goodTriplets(n = 2)
print(data)