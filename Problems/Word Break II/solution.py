import io
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo={}
        def beakTrack(s):
            if not s:
                return [[]]
            if s in memo:
                return memo[s]
            cur_word_breaks=[]
            
            for i in range(len(s)):
                new_word=s[:i+1]
                
                if new_word in wordDict:
                    rest_word_breaks=beakTrack(s[i+1:])
                    for word_break in rest_word_breaks:
                        cur_word_breaks.append([new_word]+word_break)
                        
            memo[s]=cur_word_breaks
            return cur_word_breaks
        wordSet=set(wordDict)
        word_breaks=beakTrack(s)
        return [" ".join(word_break) for word_break in word_breaks]

obj = Solution()
#data = obj.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"])
#data = obj.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])
data = obj.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])
print(data)