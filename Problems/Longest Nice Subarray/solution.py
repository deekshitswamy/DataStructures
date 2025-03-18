import io
from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        last = 0; max_len = 0; count = 0
        index = 0; i = 0

        while i < len(nums):

            while i < len(nums) and last ^ nums[i] == last + nums[i]:
                last += nums[i]
                count += 1
                i += 1
    
            max_len = max(max_len, count)
            count -= 1
            last -= nums[index]
            index += 1

        return max_len

obj = Solution()
#data = obj.longestNiceSubarray(nums = [1,3,8,48,10])
data = obj.longestNiceSubarray(nums = [3,1,5,11,13])
print(data)