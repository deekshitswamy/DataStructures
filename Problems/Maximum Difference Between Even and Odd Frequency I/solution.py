import io
from typing import List
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven

obj = Solution()
#data = obj.maxDifference(s = "aaaaabbc")
data = obj.maxDifference(s = "abcabcab")
print(data)