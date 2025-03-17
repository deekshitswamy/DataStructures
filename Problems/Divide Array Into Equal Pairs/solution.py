import io
from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        result ={}
        for j in nums:
            if j in result:
                result[j] += 1
            else:
                result[j] = 1
        return all(e % 2 == 0 for e in result.values())

obj = Solution()
#data = obj.divideArray(nums = [3,2,3,2,2,2])
data = obj.divideArray(nums = [1,2,3,4])
print(data)