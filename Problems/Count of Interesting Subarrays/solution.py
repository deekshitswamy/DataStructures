import io
from typing import List
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        current = 0
        data = Counter()
        for elem in nums:
            if elem % modulo == k:
                current = (current + 1) % modulo
            data[current] += 1

        result = current = 0
        for elem in nums:            
            result += data[(current + k) % modulo]
            if elem % modulo == k:
                current = (current + 1) % modulo
            data[current] -= 1
        return result

obj = Solution()
#data = obj.countInterestingSubarrays(nums = [3,2,4], modulo = 2, k = 1)
data = obj.countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)
print(data)