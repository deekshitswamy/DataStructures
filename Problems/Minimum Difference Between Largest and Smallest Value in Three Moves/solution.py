import io
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=4:
            return 0
        nums.sort()    
        ans=min(nums[n-1]-nums[3],nums[n-2]-nums[2],nums[n-3]-nums[1],nums[n-4]-nums[0])
        return ans

obj = Solution()
#data = obj.minDifference(nums = [5,3,2,4])
#data = obj.minDifference(nums = [1,5,0,10,14])
data = obj.minDifference(nums = [3,100,20])
print(data)