import io
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        left=0
        right=0
        dist=0
        ans=0
        while right<n:
            if right>0 and nums[right]!=nums[right-1]:
                dist+=(right-left)*(nums[right]-nums[right-1])
            right+=1
            while dist>k:
                dist-=nums[right-1]-nums[left]
                left+=1
            if right-left>ans:
                ans=right-left
        return ans

obj = Solution()
#data = obj.maxFrequency(nums = [1,2,4], k = 5)
#data = obj.maxFrequency(nums = [1,4,8,13], k = 5)
data = obj.maxFrequency(nums = [3,9,6], k = 2)
print(data)