import io
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n, ans = len(nums), 0
        count, _sum, r = 0, 0, 0
        for l in range(n):
            while r < n and (_sum + nums[r]) * (count + 1) < k:
                _sum += nums[r]
                r += 1
                count += 1

            ans += count
            _sum -= nums[l]
            count -= 1

        return ans

obj = Solution()
#data = obj.countSubarrays(n = 1)
#data = obj.countSubarrays(n = 2)
data = obj.countSubarrays(n = 2)
print(data)