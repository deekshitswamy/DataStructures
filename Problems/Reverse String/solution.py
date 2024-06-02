import io
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0,len(s)//2):
            s[i], s[-i-1] = s[-i-1],s[i]
        return s

obj = Solution()
#data = obj.reverseString(s = ["h","e","l","l","o"])
data = obj.reverseString(s = ["H","a","n","n","a","h"])
print(data)