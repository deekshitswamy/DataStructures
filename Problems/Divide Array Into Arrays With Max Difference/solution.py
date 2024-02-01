import io
from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(2,n,3):
            if nums[i]-nums[i-2]>k:
                return []
            else:
                ans.append(nums[i-2:i+1])
        return ans

obj = Solution()
#data = obj.divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2)
data = obj.divideArray(nums = [1,3,3,2,7,3], k = 3)
print(data)