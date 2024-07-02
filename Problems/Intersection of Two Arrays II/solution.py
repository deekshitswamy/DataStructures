import io
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j=0,0
        ans=[]
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans

obj = Solution()
#data = obj.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
data = obj.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(data)