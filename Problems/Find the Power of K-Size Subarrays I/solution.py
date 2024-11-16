import io
from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        count = 0
        max_val = nums[0]
        
        for i in range(k - 1):
            if nums[i] == nums[i + 1] - 1:
                max_val += 1
            else:
                count = i + 1
                max_val = nums[i + 1]

        res = []
        if count > 0:
            res.append(-1)
        else:
            res.append(max_val)

        for i in range(k, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                max_val += 1
                count -= 1
            else:
                count = k - 1
                max_val = nums[i]

            if count > 0:
                res.append(-1)
            else:
                res.append(max_val)
        
        return res

obj = Solution()
#data = obj.resultsArray(nums = [1,2,3,4,3,2,5], k = 3)
#data = obj.resultsArray(nums = [2,2,2,2,2], k = 4)
data = obj.resultsArray(nums = [3,2,3,2,3,2], k = 2)
print(data)