import io
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        count=0
        ans=0
        for j in range(n):
            if nums[j] & 1:
                k-=1
                count=0
            while k==0:
                k+= nums[i] & 1
                i+=1
                count+=1
            ans+=count
        return ans

obj = Solution()
#data = obj.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)
#data = obj.numberOfSubarrays(nums = [2,4,6], k = 1)
data = obj.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)
print(data)