import io
from typing import List
from heapq import nlargest
from collections import Counter
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        topk = nlargest(k, nums)
        count = Counter(topk)
        res = []
        for num in nums:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res

obj = Solution()
#data = obj.maxSubsequence(nums = [2,1,3,3], k = 2)
#data = obj.maxSubsequence(nums = [-1,-2,3,4], k = 3)
data = obj.maxSubsequence(nums = [3,4,3,3], k = 2)
print(data)