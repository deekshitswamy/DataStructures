import io
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        pass

obj = Solution()
#data = obj.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"])
#data = obj.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])
data = obj.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
print(data)