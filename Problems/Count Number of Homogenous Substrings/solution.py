import io
from typing import List
from itertools import groupby

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=10**9+7
        ans=0
        for x,y in groupby(s):
            n=len(list(y))
            ans+=n*(n+1)//2
        return ans%mod

obj = Solution()
#data = obj.countHomogenous(s = "abbcccaa")
#data = obj.countHomogenous(s = "xy")
data = obj.countHomogenous(s = "zzzzz")
print(data)