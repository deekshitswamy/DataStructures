import io
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's Voting Algorithm
        count=0
        result=0
        for n in nums:
            if count==0:
                result=n
            if n==result:
                count+=1
            else:
                count-=1
        return result

obj = Solution()
#data = obj.majorityElement(nums = [3,2,3])
data = obj.majorityElement(nums = [2,2,1,1,1,2,2])
print(data)