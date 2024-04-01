import io
from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        length=0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1
        return length

obj = Solution()
#data = obj.lengthOfLastWord(s = "Hello World")
#data = obj.lengthOfLastWord(s = "   fly me   to   the moon  ")
data = obj.lengthOfLastWord(s = "luffy is still joyboy")
print(data)