import io
from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            x = str(i)
            if (len(x)%2==0):
                count += 1

        return count

obj = Solution()
#data = obj.findNumbers(nums = [12,345,2,6,7896])
data = obj.findNumbers(nums = [555,901,482,1771])
print(data)