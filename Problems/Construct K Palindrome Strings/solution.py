import io
from typing import Counter, List
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        return odd_count <= k <= len(s)

obj = Solution()
#data = obj.canConstruct(s = "annabelle", k = 2)
#data = obj.canConstruct(s = "leetcode", k = 3)
data = obj.canConstruct(s = "true", k = 4)
print(data)