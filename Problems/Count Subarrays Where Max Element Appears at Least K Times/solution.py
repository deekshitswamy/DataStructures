import io
from typing import List
from collections import Counter
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num=max(nums)
        freq=Counter()
        ans=i=0
        for j in nums:
            freq[j]+=1
            while freq[max_num]>=k:
                freq[nums[i]]-=1

                i+=1
            ans+=i
        return ans

obj = Solution()
#data = obj.countSubarrays(nums = [1,3,2,3,3], k = 2)
data = obj.countSubarrays(nums = [1,4,2,1], k = 3)
print(data)