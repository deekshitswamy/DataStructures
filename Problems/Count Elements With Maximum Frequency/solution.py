import io
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        list_nums=list(set(nums))
        freq=0
        for i in list_nums:
            freq=max(freq,nums.count(i))
        ans=0
        for i in list_nums:
            if nums.count(i)==freq:
                ans+=freq

        return ans

obj = Solution()
#data = obj.maxFrequencyElements(nums = [1,2,2,3,1,4])
data = obj.maxFrequencyElements(nums = [1,2,3,4,5])
print(data)