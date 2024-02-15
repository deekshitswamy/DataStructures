import io
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_of_nums=sum(nums)
        n=len(nums)
        for i in range(n-1,1,-1):
            sum_of_nums-=nums[i]
            if sum_of_nums>nums[i]:
                return sum_of_nums+nums[i]
        return -1

obj = Solution()
#data = obj.largestPerimeter(nums = [5,5,5])
#data = obj.largestPerimeter(nums = [1,12,1,2,5,50,3])
data = obj.largestPerimeter(nums = [5,5,50])
print(data)