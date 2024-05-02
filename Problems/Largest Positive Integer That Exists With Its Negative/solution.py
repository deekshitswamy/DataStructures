import io
from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1
        nums.sort()
        while l < r:
            if -nums[l] == nums[r]:
                return nums[r]
            if abs(nums[l]) > abs(nums[r]):
                l+=1
            else:
                r-=1     
        return -1

obj = Solution()
#data = obj.findMaxK(nums = [-1,2,-3,3])
#data = obj.findMaxK(nums = [-1,10,6,7,-7,1])
data = obj.findMaxK(nums = [-10,8,6,7,-2,-3])
print(data)