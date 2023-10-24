import io
from cmath import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return n>0 and log(n,4).is_integer()

obj = Solution()
#data = obj.isPowerOfFour(n = 16)
#data = obj.isPowerOfFour(n = 5)
data = obj.isPowerOfFour(n = 1)
print(data)