import io
from typing import List
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index=word.index(ch)
        return word[:index+1][::-1]+word[index+1:]

obj = Solution()
#data = obj.reversePrefix(word = "abcdefd", ch = "d")
#data = obj.reversePrefix(word = "xyxzxe", ch = "z")
data = obj.reversePrefix(word = "abcd", ch = "z")
print(data)