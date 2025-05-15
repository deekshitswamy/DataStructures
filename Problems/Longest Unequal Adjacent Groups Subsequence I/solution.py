import io
from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        lis=[]
        lis.append(words[0])
        for i in range(len(groups)-1):
            if groups[i]!=groups[i+1]:
                lis.append(words[i+1])
        return lis

obj = Solution()
#data = obj.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1])
data = obj.getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1])
print(data)