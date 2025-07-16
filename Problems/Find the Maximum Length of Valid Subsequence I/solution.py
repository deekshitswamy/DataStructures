import io
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_cnt = even_cnt = diff_cnt = 0
        prev = nums[0]
        for num in nums:
            if num % 2:
                odd_cnt += 1
            else:
                even_cnt += 1

            if (num + prev) % 2:
                diff_cnt += 1
                prev = num

        return max(odd_cnt, even_cnt, diff_cnt+1)

obj = Solution()
#data = obj.maximumLength(nums = [1,2,3,4])
#data = obj.maximumLength(nums = [1,2,1,1,2,1,2])
data = obj.maximumLength(nums = [1,3])
print(data)