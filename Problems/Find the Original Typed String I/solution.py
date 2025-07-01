import io
from typing import List
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=1
        start=0
        end=len(word)

        while start<end:
            idx=start
            while idx<end and word[idx]==word[start]:
                idx+=1
            ans+=(idx-start-1)
            start=idx
        return ans

obj = Solution()
#data = obj.possibleStringCount(word = "abbcccc")
#data = obj.possibleStringCount(word = "abcd")
data = obj.possibleStringCount(word = "aaaa")
print(data)