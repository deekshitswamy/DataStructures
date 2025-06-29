import io
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = 0
        modulo = 10 ** 9 + 7

        j = len(nums) - 1
        for i, elem in enumerate(nums):
            while i <= j and elem + nums[j] > target:
                j -= 1
            if i > j:
                break
            result = (result + pow(2, j - i, modulo)) % modulo
        
        return result % modulo

obj = Solution()
#data = obj.numSubseq(nums = [3,5,6,7], target = 9)
#data = obj.numSubseq(nums = [3,3,6,8], target = 10)
data = obj.numSubseq(nums = [2,3,3,4,6,7], target = 12)
print(data)