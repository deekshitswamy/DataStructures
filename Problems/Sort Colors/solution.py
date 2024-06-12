import io
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Dutch national flag problem (red, white, blue)
        l, m, r = 0, 0, len(nums) - 1  # pointers to partition

        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:  # nums[m] == 2
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1

obj = Solution()
#data = obj.sortColors(nums = [2,0,2,1,1,0])
data = obj.sortColors(nums = [2,0,1])
print(data)