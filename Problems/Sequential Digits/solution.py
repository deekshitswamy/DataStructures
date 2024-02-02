import io
from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        res = []
        l1 = len(str(low))
        l2 = len(str(high))
        for i in range(l1,l2+1):
            l = 0
            r = i
            while r<=len(s):
                val = int(s[l:r])
                if val in range(low, high+1):
                    res.append(val)
                l += 1
                r += 1 
        return res

obj = Solution()
#data = obj.sequentialDigitslow = 100, high = 300)
data = obj.sequentialDigits(low = 1000, high = 13000)
print(data)