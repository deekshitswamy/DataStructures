import io
from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        totalsum=mean*(n+m)
        missingsum=totalsum-sum(rolls)
        if missingsum>6*n or missingsum<n:
            return []
        res=[]
        while n:
            curr=min(6,missingsum-n+1)
            res.append(curr)
            missingsum-=curr
            n-=1
        return res

obj = Solution()
#data = obj.missingRolls(rolls = [3,2,4,3], mean = 4, n = 2)
#data = obj.missingRolls(rolls = [1,5,6], mean = 3, n = 4)
data = obj.missingRolls(rolls = [1,2,3,4], mean = 6, n = 4)
print(data)