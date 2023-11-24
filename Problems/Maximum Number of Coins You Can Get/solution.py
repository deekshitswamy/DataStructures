import io
import collections
from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q=collections.deque(piles)
        ans=0
        while len(q)>0:
            q.popleft()
            q.pop()
            ans+=q[-1]
            q.pop()
        return ans

obj = Solution()
#data = obj.maxCoins(piles = [2,4,1,2,7,8])
#data = obj.maxCoins(piles = [2,4,5])
data = obj.maxCoins(piles = [9,8,7,6,5,1,2,3,4])
print(data)