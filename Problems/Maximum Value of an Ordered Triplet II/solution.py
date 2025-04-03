import io
from typing import List
from itertools import accumulate
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        leftMax = list(accumulate(nums, max))
        rightMax = list(accumulate(reversed(nums), max))[::-1]
        maxAns = 0

        for i in range(1, len(nums) - 1):
            maxAns = max(maxAns, (leftMax[i - 1] - nums[i]) * rightMax[i + 1])
        
        return maxAns

obj = Solution()
#data = obj.maximumTripletValue(nums = [12,6,1,2,7])
#data = obj.maximumTripletValue(nums = [1,10,3,4,19])
data = obj.maximumTripletValue(nums = [1,2,3])
print(data)