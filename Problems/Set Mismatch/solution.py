import io
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumtoN = n*(n+1)//2
        missingNum = sumtoN - sum(set(nums))
        duplicateNum = sum(nums) - (sumtoN - missingNum)
        return [duplicateNum,missingNum]

obj = Solution()
#data = obj.findErrorNums(nums = [1,2,2,4])
data = obj.findErrorNums(nums = [1,1])
print(data)