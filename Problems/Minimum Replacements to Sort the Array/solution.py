import io
from math import ceil
from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        prev=10**9+1
        for x in nums[::-1]:
            d=ceil(x/prev)
            ans+=d-1
            prev=x//d

        return ans 
obj = Solution()
#data = obj.minimumReplacement(nums = [3,9,3])
data = obj.minimumReplacement(nums = [1,2,3,4,5])
print(data)