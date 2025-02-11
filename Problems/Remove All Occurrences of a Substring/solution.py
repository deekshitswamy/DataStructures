import io
from typing import List
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s

obj = Solution()
#data = obj.removeOccurrences(s = "daabcbaabcbc", part = "abc")
data = obj.removeOccurrences(s = "axxxxyyyyb", part = "xy")
print(data)