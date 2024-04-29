import io
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=0
        for i in nums:
            ans^=i
            
        ans=ans^k
        return bin(ans).count('1')

obj = Solution()
#data = obj.minOperations(nums = [2,1,3,4], k = 1)
data = obj.minOperations(nums = [2,0,2,0], k = 0)
print(data)