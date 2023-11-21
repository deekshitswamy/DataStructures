import io
import collections
from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=10**9+7
        ans=0
        count=collections.Counter()
        for num in nums:
            num-=int(str(num)[::-1])
            ans+=count[num]
            count[num]+=1
        return ans%mod

obj = Solution()
#data = obj.countNicePairs(nums = [42,11,1,97])
data = obj.countNicePairs(nums = [13,10,35,24,76])
print(data)