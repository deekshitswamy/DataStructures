import io
from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0):return 0
        if(n==1):return nums[0]
        sum,ans=nums[0],0
        for i in range(0,n-1):
            if nums[i+1]>nums[i]:
                sum+=nums[i+1]
            else:
                ans=max(sum,ans)
                sum=nums[i+1]
            ans=max(sum,ans)
        return ans

obj = Solution()
#data = obj.maxAscendingSum(nums = [10,20,30,5,10,50])
#data = obj.maxAscendingSum(nums = [10,20,30,40,50])
data = obj.maxAscendingSum(nums = [12,17,15,13,10,11,12])
print(data)