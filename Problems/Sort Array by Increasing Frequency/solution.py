import io
from typing import List
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num_frequency = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (num_frequency[x], -x))
        return sorted_nums

obj = Solution()
#data = obj.frequencySort(nums = [1,1,2,2,2,3])
#data = obj.frequencySort(nums = [2,3,1,3,2])
data = obj.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1])
print(data)