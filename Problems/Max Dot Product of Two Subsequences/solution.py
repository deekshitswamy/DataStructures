import io
from math import inf
from typing import List
from functools import cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        @cache
        def dp(i,j):
            if i==n1 or j==n2:
                return -inf
            return max(nums1[i]*nums2[j] +dp(i+1,j+1),nums1[i]*nums2[j], dp(i+1,j),dp(i,j+1))
        return dp(0,0)

obj = Solution()
#data = obj.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])
#data = obj.maxDotProduct(nums1 = [3,-2], nums2 = [2,-6,7])
data = obj.maxDotProduct(nums1 = [-1,-1], nums2 = [1,1])
print(data)