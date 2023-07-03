import io
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target:int)->List:
        index_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    index_list=[i,j]
                    break
        return index_list
    
obj = Solution()
data = obj.twoSum(nums=[1,2,3,4,5], target=8)
print(data)