import io
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            ans.append(x**2)
        return sorted(ans)

obj = Solution()
#data = obj.sortedSquares(nums = [-4,-1,0,3,10])
data = obj.sortedSquares(nums = [-7,-3,2,3,11])
print(data)