import io
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        freq=[0]*n

        for i in range(n):
            if freq[nums[i]]==0:
                freq[nums[i]]+=1
            else:
                return nums[i]

obj = Solution()
#data = obj.findDuplicate(nums = [1,3,4,2,2])
data = obj.findDuplicate(nums = [3,1,3,4,2])
print(data)