import io
from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1=nums1
        num2=nums2
        if len(num1)%2==0 and len(num2)%2==0:
            return 0
        elif len(num2)%2==0:
            x=0
            for i in num2:
                x^=i
            return x
        elif len(num1)%2==0:
            x=0
            for i in num1:
                x^=i
            return x
        else:
            x=0
            for i in num2:
                x^=i
            for i in num1:
                x^=i
            return x

obj = Solution()
#data = obj.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0])
data = obj.xorAllNums(nums1 = [1,2], nums2 = [3,4])
print(data)