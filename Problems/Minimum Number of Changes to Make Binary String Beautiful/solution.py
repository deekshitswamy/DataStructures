import io
from typing import List
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s) 
        c= 0
        for i in range(0,n,2):
            if s[i]!=s[i+1]:
                c+=1
        return c

obj = Solution()
#data = obj.minChanges(s = "1001")
#data = obj.minChanges(s = "10")
data = obj.minChanges(s = "0000")
print(data)