import io
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        seen=[]
        ans=[]   
        for i in range(n):
            if seen and seen[0]==i-k:
                seen.pop(0)

            while seen and nums[seen[-1]]<nums[i]:
                seen.pop()

            seen.append(i)
            if i>=k-1:
                ans.append(nums[seen[0]])
        return ans

obj = Solution()
data = obj.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
#data = obj.maxSlidingWindow(nums = [1], k = 1)
print(data)