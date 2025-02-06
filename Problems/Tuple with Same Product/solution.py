import io
from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        record = {}
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                record[product] = record.get(product, 0) + 1
        result = 0
        for _, value in record.items():
            if value >= 2:
                result += value * (value-1) // 2 * 8
        return result

obj = Solution()
#data = obj.tupleSameProduct(nums = [2,3,4,6])
data = obj.tupleSameProduct(nums = [1,2,4,5,10])
print(data)