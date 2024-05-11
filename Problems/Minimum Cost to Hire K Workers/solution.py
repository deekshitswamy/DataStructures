import io
from typing import List
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans=inf
        rsm=0
        stack=[]
        for q,w in sorted(zip(quality,wage),key=lambda x:x[1]/x[0]):
            rsm+=q
            heappush(stack,-q)
            if len(stack)>k:
                rsm+=heappop(stack)
            if len(stack)==k:
                ans=min(ans,rsm*w/q)
        return ans

obj = Solution()
#data = obj.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2)
data = obj.mincostToHireWorkers(quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3)
print(data)