import io
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        json_num_frequencies = dict()
        for i in nums:
            if json_num_frequencies.get(i) == None:
                json_num_frequencies[i] = 0
            json_num_frequencies[i] += 1
        for x, freq in json_num_frequencies.items():
            if freq == 1:
                return x
        return -1

obj = Solution()
data = obj.singleNumber(nums = [2,2,3,2])
#data = obj.singleNumber(nums = [0,1,0,1,0,1,99])
print(data)