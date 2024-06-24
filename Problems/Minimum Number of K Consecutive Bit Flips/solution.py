import io
from typing import List
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur=0
        ans=0
        n =len(nums)
        for i in range(n):
            if i >=k and nums[i-k] > 1:
                nums[i-k]-= 2
                cur-=1
            if cur & 1 ^ nums[i]==0:
                if i+k>n:
                    return -1
                nums[i]+=2
                cur+=1
                ans+=1
        return ans

obj = Solution()
#data = obj.minKBitFlips(nums = [0,1,0], k = 1)
#data = obj.minKBitFlips(nums = [1,1,0], k = 2)
data = obj.minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3)
print(data)