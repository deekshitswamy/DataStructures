import io
from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        ans=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

obj = Solution()
#data = obj.stringMatching(words = ["mass","as","hero","superhero"])
#data = obj.stringMatching(words = ["leetcode","et","code"])
data = obj.stringMatching(words = ["blue","green","bu"])
print(data)