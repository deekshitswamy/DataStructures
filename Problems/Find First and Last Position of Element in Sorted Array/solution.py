import io
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        if target in nums:
            for i in range(0,n):
                if nums[left]==nums[right]:
                    return [left,right] 
                elif nums[left]<target:
                    left+=1
                else:
                    right-=1
        else:
            return [-1,-1]

obj = Solution()
#data = obj.searchRange(nums = [5,7,7,8,8,10], target = 8)
data = obj.searchRange(nums = [5,7,7,8,8,10], target = 6)
data = obj.searchRange(nums = [], target = 0)
print(data)