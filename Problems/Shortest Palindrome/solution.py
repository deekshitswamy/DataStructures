import io
from typing import List
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=len(s)-1
        a=""
        if s==s[::-1]:
            return s
        while i!=0:
            a+=s[i]
            if a+s==(a+s)[::-1]:
                return a+s  
            i-=1  
        return a+s

obj = Solution()
#data = obj.shortestPalindrome(s = "aacecaaa")
data = obj.shortestPalindrome(s = "abcd")
print(data)