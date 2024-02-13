import io
from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            l = 0
            r = len(w) - 1
            isPal = True
            while l < r:
                if w[l] != w[r]:
                    isPal = False
                    break
                l += 1
                r -= 1

            if isPal:
                return w
                
        return ""

obj = Solution()
#data = obj.firstPalindrome(words = ["abc","car","ada","racecar","cool"])
#data = obj.firstPalindrome(words = ["notapalindrome","racecar"])
data = obj.firstPalindrome(words = ["def","ghi"])
print(data)