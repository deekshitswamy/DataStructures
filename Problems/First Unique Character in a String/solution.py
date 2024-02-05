import io
from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1

obj = Solution()
#data = obj.firstUniqChar(s = "leetcode")
#data = obj.firstUniqChar(s = "loveleetcode")
data = obj.firstUniqChar(s = "aabb")
print(data)