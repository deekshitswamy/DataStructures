import io
from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        move=0
        ans=0
        for i in nums:
            ans+=max(move-i,0)
            move=max(move+1,i+1)
        return ans 

obj = Solution()
#data = obj.minIncrementForUnique(nums = [1,2,2])
data = obj.minIncrementForUnique(nums = [3,2,1,2,1,7])
print(data)