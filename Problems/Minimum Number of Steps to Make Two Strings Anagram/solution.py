import io
from typing import List
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t)-Counter(s)).values())

obj = Solution()
#data = obj.minSteps(s = "bab", t = "aba")
#data = obj.minSteps(s = "leetcode", t = "practice")
data = obj.minSteps(s = "anagram", t = "mangaar")
print(data)