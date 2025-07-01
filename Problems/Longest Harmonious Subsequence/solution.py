import io
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        countOfnums = Counter(nums)
        max_length = 0
        for key in countOfnums.keys() :
            if key + 1 in countOfnums.keys() :
                max_length = max(max_length, countOfnums[key] + countOfnums[key + 1])
        return max_length

obj = Solution()
#data = obj.findLHS(nums = [1,3,2,2,5,2,3,7])
#data = obj.findLHS(nums = [1,2,3,4])
data = obj.findLHS(nums = [1,1,1,1])
print(data)