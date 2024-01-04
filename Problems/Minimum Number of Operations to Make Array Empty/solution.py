import io
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=Counter(nums).values()
        ans=0
        for i in count:
            if i==1:
                return -1
            else:
                ans+=i//3 + (i%3!=0)
        return ans

obj = Solution()
#data = obj.minOperations(nums = [2,3,3,2,2,4,2,3,4])
data = obj.minOperations(nums = [2,1,2,2,3,3])
print(data)