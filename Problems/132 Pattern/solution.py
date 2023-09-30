import io
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        curMin=nums[0]
        for num in nums:
            while stack and num>=stack[-1][0]:
                stack.pop()

            if stack and num>stack[-1][1]:
                return True

            stack.append([num,curMin])
            curMin=min(curMin,num)
        return False 


obj = Solution()
#data = obj.find132pattern(nums = [1,2,3,4])
#data = obj.find132pattern(nums = [3,1,4,2])
data = obj.find132pattern(nums = [-1,3,2,0])
print(data)