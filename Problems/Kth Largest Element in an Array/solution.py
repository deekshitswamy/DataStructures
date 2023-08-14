import io
import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot=random.choice(nums)
        left=[x for x in nums if x>pivot]
        mid=[x for x in nums if x==pivot]
        right=[x for x in nums if x<pivot]
        n=len(left)
        m=len(mid)
        if k<=n:
            return self.findKthLargest(left,k)

        elif k>(n+m):
            return self.findKthLargest(right,k-(n+m))

        else:
            return mid[0] 

obj = Solution()
#data = obj.findKthLargest(nums = [3,2,1,5,6,4], k = 2)
data = obj.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)
print(data)