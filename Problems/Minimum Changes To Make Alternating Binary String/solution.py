import io
from typing import List
class Solution:
    def minOperations(self, s: str) -> int:
        ans1=ans2=0
        for idx,x in enumerate(s):
            if idx%2==int(x):
                ans1+=1
            else:
                ans2+=1
        return min(ans1,ans2)

obj = Solution()
#data = obj.minOperations(s = "0100")
#data = obj.minOperations(s = "10")
data = obj.minOperations(s = "1111")
print(data)