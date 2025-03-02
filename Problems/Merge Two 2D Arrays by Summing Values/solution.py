import io
from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1 = dict(nums1)
        nums2 = dict(nums2)
        ms = nums1.keys() | nums2.keys()
        lst = []
        for k in sorted(ms):
            lst.append([k, nums1.get(k,0)+nums2.get(k,0)])
        return lst

obj = Solution()
#data = obj.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]])
data = obj.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]])
print(data)