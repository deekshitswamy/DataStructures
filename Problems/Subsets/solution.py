import io
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        subset=[]
        def dfs(i):
            if i>=n:
                ans.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return ans

obj = Solution()
#data = obj.subsets(nums = [1,2,3])
data = obj.subsets(nums = [0])
print(data)