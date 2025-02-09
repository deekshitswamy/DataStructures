import io
from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for i, num in enumerate(nums):
            m[i - num] += 1
        
        n = len(nums)
        res = n * (n - 1) // 2
        
        for v in m.values():
            res -= v * (v - 1) // 2
        
        return res

obj = Solution()
#data = obj.countBadPairs(nums = [4,1,3,3])
data = obj.countBadPairs(nums = [1,2,3,4,5])
print(data)