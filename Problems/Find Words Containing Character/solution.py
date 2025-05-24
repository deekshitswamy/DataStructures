import io
from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]

obj = Solution()
#data = obj.findWordsContaining(words = ["leet","code"], x = "e")
#data = obj.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a")
data = obj.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z")
print(data)