import io
from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n=len(nums)
        def good(left,right):
            k=list(sorted(nums[left:right+1]))
            if len(k)==1:
                return True
            delta=k[1]-k[0]
            for i,j in zip(k,k[1:]):
                if (abs(i-j))!=delta:
                    return False
            return True
        ans=[]
        for left,right in zip(l,r):
            ans+=[good(left,right)]
        return ans

obj = Solution()
#data = obj.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
data = obj.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10])
print(data)