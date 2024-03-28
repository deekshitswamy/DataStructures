import io
from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        start=0
        end=0
        ans=0
        freq={}
        while end<n:
            freq[nums[end]]=freq.get(nums[end],0)+1
            while freq[nums[end]]>k:
                freq[nums[start]]-=1
                start+=1
            ans=max(ans,end-start+1)
            end+=1  
        return ans

obj = Solution()
#data = obj.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2)
#data = obj.maxSubarrayLength(nums = [1,2,1,2,1,2,1,2], k = 1)
data = obj.maxSubarrayLength(nums = [5,5,5,5,5,5,5], k = 4)
print(data)