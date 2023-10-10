import io
import sys
from typing import List
from bisect import bisect_right
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums=sorted(set(nums))
        ans=sys.maxsize
        for i,s in enumerate(nums):
            e=s+n-1
            idx=bisect_right(nums,e)
            ans=min(ans,n-idx+i)
        return ans    

obj = Solution()
#data = obj.minOperations(nums = [4,2,5,3])
#data = obj.minOperations(nums = [1,2,3,5,6])
data = obj.minOperations(nums = [1,10,100,1000])
print(data)