import io
from typing import List
from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n=len(s)
        @cache
        def dp(i:int,extra:int)->int:
            if i>=n:
                return extra

            min_extra=dp(i+1,extra)
            for word in dictionary:
                if s[i:].startswith(word):
                    min_extra=min(min_extra,dp(i+len(word),extra-len(word)))

            return min_extra
        return dp(0,n)

obj = Solution()
#data = obj.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])
data = obj.minExtraChar(s = "sayhelloworld", dictionary = ["hello","world"])
print(data)
