import io
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left,right=0,len(nums)
        nums.sort()
        while left<=right:
            mid=(left+right)//2
            if mid>len(nums)-1:
                return mid
            elif mid!=nums[mid] and mid<len(nums):
                right=mid-1
            elif mid==nums[mid]:
                left=mid+1
        return left

obj = Solution()
#data = obj.missingNumber(nums = [3,0,1])
#data = obj.missingNumber(nums = [0,1])
data = obj.missingNumber(nums = [9,6,4,2,3,5,7,0,1])
print(data)