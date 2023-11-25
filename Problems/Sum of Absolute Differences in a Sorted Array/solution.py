import io
from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        total=0
        for num in nums:
            total+=abs(num-nums[0])
        ans.append(total)
        for idx in range(1,n):
            res=nums[idx]-nums[idx-1]
            total+=res*idx
            total-=res*(n-idx)
            ans.append(total)
        return ans

obj = Solution()
#data = obj.getSumAbsoluteDifferences(nums = [2,3,5])
data = obj.getSumAbsoluteDifferences(nums = [1,4,6,8,10])
print(data)