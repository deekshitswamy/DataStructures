import io
import collections
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=collections.Counter(words[0])
        for word in words:
            ans &=collections.Counter(word)
        return list(ans.elements())

obj = Solution()
#data = obj.commonChars(words = ["bella","label","roller"])
data = obj.commonChars(words = ["cool","lock","cook"])
print(data)