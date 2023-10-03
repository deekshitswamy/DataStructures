import io
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    count+=1
        return count

obj = Solution()
#data = obj.numIdenticalPairs(nums = [1,2,3,1,1,3])
#data = obj.numIdenticalPairs(nums = [1,1,1,1])
data = obj.numIdenticalPairs(nums = [1,2,3])
print(data)