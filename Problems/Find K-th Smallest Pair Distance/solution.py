import io
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairs(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = countPairs(nums, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

obj = Solution()
#data = obj.smallestDistancePair(nums = [1,3,1], k = 1)
#data = obj.smallestDistancePair(nums = [1,1,1], k = 2)
data = obj.smallestDistancePair(nums = [1,6,1], k = 3)
print(data)