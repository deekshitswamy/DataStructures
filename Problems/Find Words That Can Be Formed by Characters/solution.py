import io
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    break
            else: count+=len(word)
        return count

obj = Solution()
#data = obj.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach")
data = obj.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
print(data)