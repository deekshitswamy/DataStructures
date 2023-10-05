import io
from typing import List

class Solution:
        def majorityElement(self, nums: List[int]) -> List[int]:
            n = list(set(nums))
            l = len(nums)//3
            res = []

            for i in n:
                if nums.count(i) > l:
                    res.append(i)
            
            return res

obj = Solution()
#data = obj.majorityElement(nums = [3,2,3])
#data = obj.majorityElement(nums = [1])
data = obj.majorityElement(nums = [1,2])
print(data)