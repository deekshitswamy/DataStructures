import io
from typing import List
class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)
        ans=0
        zeroes=0
        ones=s.count('1')
        for i in range(n-1):
            if s[i]=='0':
                zeroes+=1
            else:
                ones-=1
            ans=max(ans,ones+zeroes)
        return ans

obj = Solution()
#data = obj.maxScore(s = "011101")
#data = obj.maxScore(s = "00111")
data = obj.maxScore(s = "1111")

print(data)