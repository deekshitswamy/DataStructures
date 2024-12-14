import io
from typing import List
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 1 
        left = nums[0] - 2
        right = nums[0] + 2
        l = 0
        for r in range(1, len(nums)):
            if left <= nums[r] <= right:
                left = max(left, nums[r] - 2)
                right = min(right, nums[r] + 2)
            else:
                left = nums[r] - 2
                right = nums[r] + 2
                l = r
                while nums[r] - 2 <= nums[l] <= nums[r] + 2:
                    left = max(left, nums[l] - 2)
                    right = min(right, nums[l] + 2)
                    l -= 1
                l += 1
            ans += r - l + 1

        return ans

obj = Solution()
#data = obj.continuousSubarrays(nums = [5,4,2,4])
data = obj.continuousSubarrays(nums = [1,2,3])
print(data)