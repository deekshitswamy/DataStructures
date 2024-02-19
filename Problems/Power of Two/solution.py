import io
from typing import List
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and log2(n)==int(log2(n))

obj = Solution()
#data = obj.isPowerOfTwo(n = 1)
#data = obj.isPowerOfTwo(n = 16)
data = obj.isPowerOfTwo(n = 2)
print(data)