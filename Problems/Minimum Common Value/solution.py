import io
from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res=list(set(nums1)& set(nums2))
        if len(res)==0:
            return -1
        else:
            res.sort()
            return res[0]

obj = Solution()
#data = obj.getCommon(nums1 = [1,2,3], nums2 = [2,4])
data = obj.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5])
print(data)