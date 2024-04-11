import io
from typing import List
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans=[]
        for i in num:
            while k>0 and ans and ans[-1]>i:
                
                ans.pop()
                k-=1
            ans.append(i)
        while k>0:
            ans.pop()
            k-=1    
        
        res="".join(ans).lstrip("0")
        return res if res else "0"

obj = Solution()
#data = obj.removeKdigits(num = "1432219", k = 3)
#data = obj.removeKdigits(num = "10200", k = 1)
data = obj.removeKdigits(num = "10", k = 2)
print(data)