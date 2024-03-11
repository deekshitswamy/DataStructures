import io
from typing import List
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=defaultdict(int)
        i=0
        for c in order:
            ans[c]=i
            i+=1
        return "".join(sorted(s,key=lambda x:ans.get(x,100)))

obj = Solution()
#data = obj.customSortString(order = "cba", s = "abcd")
data = obj.customSortString(order = "bcafg", s = "abcd")
print(data)