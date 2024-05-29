import io
from typing import List
class Solution:
    def numSteps(self, s: str) -> int:
        ans=0
        num=int(s,2)
        while num!=1:
            if num%2==0:
                num=num//2
            else:
                num+=1
            ans+=1
        return ans

obj = Solution()
#data = obj.numSteps(s = "1101")
#data = obj.numSteps(s = "10")
data = obj.numSteps(s = "1")
print(data)