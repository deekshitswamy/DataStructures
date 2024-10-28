import io
from typing import List
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_streak = 0
        
        for num in nums:
            count = 0
            current = num
            while current in num_set:
                count += 1
                current = current * current
                if current > 2**31 - 1:  # Avoid overflow (INT_MAX equivalent)
                    break
            max_streak = max(max_streak, count)
        
        return max_streak if max_streak >= 2 else -1

obj = Solution()
#data = obj.longestSquareStreak(nums = [4,3,6,16,8,2])
data = obj.longestSquareStreak(nums = [2,3,5,6,7])
print(data)