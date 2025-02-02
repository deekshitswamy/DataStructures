import io
from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        lst = sorted(nums)
        for i in range(0, len(nums)):
            if lst == nums:
                return True
            ele = lst.pop(-1)
            lst.insert(0, ele)
        return False

obj = Solution()
#data = obj.check(nums = [3,4,5,1,2])
#data = obj.check(nums = [2,1,3,4])
data = obj.check(nums = [1,2,3])
print(data)