import io
from typing import List
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        l = len(s)
        a = s[0:(l//2)]
        b = s[(l//2):l]
        counta = 0
        countb = 0
        
        for i in range(l//2):
            if a[i] in vowels:
                counta += 1
            if b[i] in vowels:
                countb += 1
        if counta == countb:
            return True
        else:
            return False

obj = Solution()
#data = obj.halvesAreAlike(s = "book")
data = obj.halvesAreAlike(s = "textbook")

print(data)