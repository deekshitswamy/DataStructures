import io
from typing import List
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
            
        count1 = Counter(word1)
        count2 = Counter(word2)

        condition1 = sorted(count1.keys()) == sorted(count2.keys())
        condition2 = sorted(count1.values()) == sorted(count2.values())

        return condition1 and condition2

obj = Solution()
#data = obj.closeStrings(word1 = "abc", word2 = "bca")
#data = obj.closeStrings(word1 = "a", word2 = "aa")
data = obj.closeStrings(word1 = "cabbba", word2 = "abbccc")
print(data)