import io
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1=nums1+nums2
        list1.sort()
        length=len(list1)
        if length%2==1:
            return float(list1[((length+1)//2)-1])
        else:
            return (list1[length//2-1]+list1[(length//2)])/2                             

obj = Solution()
#data = obj.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])
data = obj.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
print(data)