import io
from typing import List
class Solution:
    def makeGood(self, s: str) -> str:
        change=True
        sr=list(s)
        
        while change and len(sr):
            i=0
            c=0
            while i<len(sr)-1 :
                if ord(sr[i])==ord(sr[i+1])+32 or ord(sr[i])==ord(sr[i+1])-32 :
                    del sr[i:i+2]
                    c+=1
                i+=1
            if c==0:
                change =False
                    
        return ''.join(sr)

obj = Solution()
#data = obj.makeGood(s = "leEeetcode")
#data = obj.makeGood(s = "leEeetcode")
data = obj.makeGood(s = "s")
print(data)