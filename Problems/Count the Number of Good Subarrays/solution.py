import io
from typing import List
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        hs = defaultdict(int)
        n = len(nums)
        right = -1
        res = 0
        pairs = 0

        for left in range(n):
            while right < n - 1 and pairs < k:
                right += 1
                pairs += hs[nums[right]]
                hs[nums[right]] += 1
            if pairs >= k:
                res += n - right

            hs[nums[left]] -= 1
            pairs -= hs[nums[left]]
        
        return res

obj = Solution()
#data = obj.countGood(nums = [1,1,1,1,1], k = 10)
data = obj.countGood(nums = [3,1,4,3,2,2,4], k = 2)
print(data)