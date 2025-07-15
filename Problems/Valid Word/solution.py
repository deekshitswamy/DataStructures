import io
from typing import List
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = set("aeiouAEIOU")
        has_vowels = False
        has_cons = False
        for c in word:
            if not (c.isalpha() or c.isdigit()):
                return False
            if c.isalpha():
                if c in vowels:
                    has_vowels = True
                else:
                    has_cons = True
        return has_vowels and has_cons

obj = Solution()
#data = obj.isValid(word = "234Adas")
#data = obj.isValid(word = "b3")
data = obj.isValid(word = "a3$e")
print(data)