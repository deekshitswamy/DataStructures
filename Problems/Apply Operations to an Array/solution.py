import io
from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            else:
                continue
        j1=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j1],nums[i]=nums[i],nums[j1]
                j1+=1
        return nums

obj = Solution()
#data = obj.applyOperations(nums = [1,2,2,1,1,0])
data = obj.applyOperations(nums = [0,1])
print(data)