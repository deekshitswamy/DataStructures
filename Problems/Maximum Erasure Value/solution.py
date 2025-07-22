import io
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = {}
        s, left, left_s, ans = 0, 0, 0, 0
        for i, num in enumerate(nums):
            if num in dic and dic[num][0] > left:
                left, left_s = dic[num]
            s += num
            ans = max(s - left_s , ans)
            dic[num] = (i+1, s)
        return ans

obj = Solution()
#data = obj.maximumUniqueSubarray(nums = [4,2,4,5,6])
data = obj.maximumUniqueSubarray(nums = [5,2,1,2,5,2,1,2,5])
print(data)