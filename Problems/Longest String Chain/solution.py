import io
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp={}
        for word in sorted(words,key=len):
            temp=[0]
            n=len(word)
            for i in range(n):
                if word[:i]+word[i+1:] in dp:
                    temp.append(dp[word[:i]+word[i+1:]])
                dp[word]=max(temp)+1
        return max(dp.values())

obj = Solution()
#data = obj.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])
data = obj.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"])
#data = obj.longestStrChain(words = ["abcd","dbqca"])
print(data)