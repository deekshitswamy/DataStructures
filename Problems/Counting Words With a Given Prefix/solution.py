import io
from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.find(pref) == 0:
                count += 1
        return count

obj = Solution()
#data = obj.prefixCount(words = ["pay","attention","practice","attend"], pref = "at")
data = obj.prefixCount(words = ["leetcode","win","loops","success"], pref = "code")
print(data)