import io
from typing import List
class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        depth=0
        for x in s:
            if x=="(":
                depth+=1
                ans=max(depth,ans)
            elif x==")":
                depth-=1
        return ans

obj = Solution()
#data = obj.maxDepth(s = "(1+(2*3)+((8)/4))+1")
data = obj.maxDepth(s = "(1)+((2))+(((3)))")
print(data)