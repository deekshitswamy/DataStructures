import io
from typing import List
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=0
        for c in s:
            x=ord(c)-96
            q,r =divmod(x, 10)
            num+=q+r
        k-=1
        x=num
        for _ in range(k, 0, -1):
            num=0
            while x>0:
                q,r =divmod(x, 10)
                num+=r
                x=q
            x=num
            if x<10:break
        return num

obj = Solution()
#data = obj.getLucky(s = "iiii", k = 1)
#data = obj.getLucky(s = "leetcode", k = 2)
data = obj.getLucky(s = "zbax", k = 2)
print(data)