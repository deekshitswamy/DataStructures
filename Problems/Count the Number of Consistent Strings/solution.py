import io
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        pass

obj = Solution()
#data = obj.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
#data = obj.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
data = obj.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])
print(data)