import io
from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        for i,r in enumerate(nums):
            for j ,val in enumerate(r):
                if len(ans)<=i+j:
                    ans.append([])
                ans[i+j].append(val)
        seen=[]
        for r in ans:
            seen+=reversed(r)
        return seen

obj = Solution()
#data = obj.findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]])
data = obj.findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
print(data)