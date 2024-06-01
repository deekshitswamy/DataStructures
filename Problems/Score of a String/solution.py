import io
from typing import List
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for x in range(0,len(s)-1):
            res = res + abs(ord(s[x])-ord(s[x+1]))
        return res

obj = Solution()
#data = obj.scoreOfString(s = "hello")
data = obj.scoreOfString(s = "zaz")
print(data)