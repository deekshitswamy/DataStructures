import io
from typing import List
class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        if n==0 or n==1:
            return n
        for i in range(2,n):
            d=a+b+c
            a=b
            b=c
            c=d
        return c

obj = Solution()
#data = obj.tribonacci(n = 4)
data = obj.tribonacci(n = 25)
print(data)