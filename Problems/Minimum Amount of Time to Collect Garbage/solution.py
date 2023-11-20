import io
from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans=0
        n=len(garbage)
        for c in "MPG":
            best=0
            cur=0
            cur+=garbage[0].count(c)
            best=max(cur,best)
            for i in range(1,n):
                cur+=travel[i-1]
                if c in garbage[i]:
                    cur+=garbage[i].count(c)
                    best=max(cur,best)
            ans+=best
        return ans

obj = Solution()
#data = obj.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3])
data = obj.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])
print(data)