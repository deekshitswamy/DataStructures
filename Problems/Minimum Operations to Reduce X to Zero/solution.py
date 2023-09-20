import io
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        target=sum(nums)-x
        dp=[0]
        res=0
        for num in nums:
            res+=num
            dp.append(res)
        seen={v:i for i,v in enumerate(dp)}
        ans=-1
        for l_val,l_idx in seen.items():
            if l_val+target in seen:
                ans=max(seen[l_val+target]-l_idx,ans)
        if ans==-1:
            return ans
        else:
            return n-ans 

obj = Solution()
#data = obj.minOperations(nums = [1,1,4,2,3], x = 5)
#data = obj.minOperations(nums = [5,6,7,8,9], x = 4)
data = obj.minOperations(nums = [3,2,20,1,1,3], x = 10)
print(data)