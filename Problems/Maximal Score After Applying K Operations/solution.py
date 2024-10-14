import io
import math
import heapq
from typing import List
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans=0
        maxi=[-n for n in nums]
        heapq.heapify(maxi)
        while k:
            n=-heapq.heappop(maxi)
            ans+=n
            k-=1
            p=-math.ceil(n/3)
            heapq.heappush(maxi,p)
        return ans

obj = Solution()
#data = obj.maxKelements(nums = [10,10,10,10,10], k = 5)
data = obj.maxKelements(nums = [1,10,3,3,3], k = 3)
print(data)