import io
from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq=[0]*(26)
        ans=0
        for c in s:
            freq[ord(c)-97]+=1
        for i in range(t):
            next_freq=[0]*26
            for j in range(26):
                c=freq[j]
                if j<=24:
                    next_freq[j+1]+=c
                elif j==25:
                    next_freq[0]+=c
                    next_freq[1]+=c
            freq=next_freq
        for i in range(26):
            ans=(ans+freq[i])%((10**9)+7)
        return ans

obj = Solution()
#data = obj.lengthAfterTransformations(s = "abcyy", t = 2)
data = obj.lengthAfterTransformations(s = "azbk", t = 1)
print(data)