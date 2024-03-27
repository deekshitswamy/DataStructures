import io
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        product=1
        ans=0
        left=0
        n=len(nums)
        for right in range(n):
            product*=nums[right]
            if product>=k:
                while product>=k and left<=right:
                    product/=nums[left]
                    left+=1
            ans+=right-left+1
        return ans

obj = Solution()
#data = obj.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
data = obj.numSubarrayProductLessThanK(nums = [1,2,3], k = 0)
print(data)