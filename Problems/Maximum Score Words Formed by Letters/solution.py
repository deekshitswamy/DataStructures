import io
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def dp(n,letter):
            ans=0
            if n==len(words):
                return 0
            ans=0
            m=letter
            for i in words[n]:
                if i not in m:
                    return dp(n+1,letter)
                m=m.replace(i,'',1)
                ans+=score[ord(i)-97]
            return max(dp(n+1,letter),ans+dp(n+1,m))
        return dp(0,''.join(letters))

obj = Solution()
#data = obj.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
#data = obj.maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
data = obj.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
print(data)