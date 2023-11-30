import io
from typing import List
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans=0
        while n:
            ans=-ans-(n^(n-1))
            n&=n-1
        return abs(ans)

obj = Solution()
#data = obj.minimumOneBitOperations(n = 3)
data = obj.minimumOneBitOperations(n = 6)
print(data)