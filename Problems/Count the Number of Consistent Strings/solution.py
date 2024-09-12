import io
from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)  # Convert allowed string to a set for O(1) lookups
        consistent_count = 0
        
        for word in words:
            if all(char in allowed_set for char in word):
                consistent_count += 1
        
        return consistent_count

obj = Solution()
#data = obj.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
#data = obj.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
data = obj.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"])
print(data)