import io
from typing import List
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(set(s))
        m=len(set(t))
        z=len(set(zip(s,t)))
        return n==m==z

obj = Solution()
#data = obj.isIsomorphic(s = "egg", t = "add")
#data = obj.isIsomorphic(s = "foo", t = "bar")
data = obj.isIsomorphic(s = "paper", t = "title")
print(data)