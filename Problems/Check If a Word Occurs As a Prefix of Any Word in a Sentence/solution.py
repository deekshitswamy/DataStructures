import io
from typing import List
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1

obj = Solution()
#data = obj.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")
#data = obj.isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro")
data = obj.isPrefixOfWord(sentence = "i am tired", searchWord = "you")
print(data)