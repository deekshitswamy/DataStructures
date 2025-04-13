import io
from typing import List
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7 
        def pow(x, n):
            if n == 0 : return 1
            res = 1
            while n :
                if n % 2 == 1:
                    res = (res * x) % mod
                x = (x*x) % mod
                n //= 2
            return res
        even = ceil(n/2)
        odd = n//2
        return (pow(5, even) * pow(4, odd)) % mod

obj = Solution()
#data = obj.countGoodNumbers(n = 1)
#data = obj.countGoodNumbers(n = 2)
data = obj.countGoodNumbers(n = 2)
print(data)