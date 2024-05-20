import io
from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(1<<n):
            cur=0
            for x in range(n):
                if (i &(1<<x))>0:
                    cur^=nums[x]
            ans+=cur
        return ans

obj = Solution()
#data = obj.subsetXORSum(nums = [1,3])
#data = obj.subsetXORSum(nums = [5,1,6])
data = obj.subsetXORSum(nums = [3,4,5,6,7,8])
print(data)