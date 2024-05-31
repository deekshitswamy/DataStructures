import io
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for num in nums:
            x^=num
        mask=x&-x
        ans1,ans2=0,0
        for num in nums:
            if num & mask:
                ans1^=num
            else:
                ans2^=num
        return [ans1,ans2]

obj = Solution()
#data = obj.singleNumber(nums = [1,2,1,3,2,5])
#data = obj.singleNumber(nums = [-1,0])
data = obj.singleNumber(nums = [0,1])
print(data)