import io
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        ans=[]
        for a,b in zip(pos,neg):
            ans.append(a)
            ans.append(b)
        return ans

obj = Solution()
#data = obj.rearrangeArray(nums = [3,1,-2,-5,2,-4])
data = obj.rearrangeArray(nums = [-1,1])
print(data)