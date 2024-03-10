import io
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

obj = Solution()
#data = obj.intersection(n = 1)
#data = obj.intersection(n = 2)
data = obj.intersection(n = 2)
print(data)