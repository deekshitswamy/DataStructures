import io
import bisect
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        i=0
        ans=[]
        for j in range(n):
            bisect.insort(ans,nums[j])
            if ans[-1]-ans[0]>limit:
                ans.pop(bisect.bisect(ans,nums[i])-1)
                i+=1
        return j-i+1

obj = Solution()
#data = obj.longestSubarray(nums = [8,2,4,7], limit = 4)
#data = obj.longestSubarray(nums = [10,1,2,4,7,2], limit = 5)
data = obj.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0)
print(data)