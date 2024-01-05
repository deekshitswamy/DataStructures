import io
from typing import List
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[nums[0]]
        for num in nums:
            res=bisect_left(ans,num)
            if res==len(ans):
                ans.append(num)
            elif ans[res]>num:
                ans[res]=num
        return len(ans)

obj = Solution()
#data = obj.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
#data = obj.lengthOfLIS(nums = [0,1,0,3,2,3])
data = obj.lengthOfLIS(nums = [7,7,7,7,7,7,7])
print(data)