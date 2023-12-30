import io
from typing import List
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chars = {}
        for w in words:
            for c in w:
                if c not in chars:
                    chars[c] = 1
                else:
                    chars[c] +=1
        for char, value in chars.items():
            if value % len(words) !=0:
                return False
        return True

obj = Solution()
#data = obj.makeEqual(words = ["abc","aabc","bc"])
data = obj.makeEqual(words = ["ab","a"])
print(data)