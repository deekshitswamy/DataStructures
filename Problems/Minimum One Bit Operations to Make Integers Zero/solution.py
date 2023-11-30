import io
from typing import List
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans
        
        """
        ans=0
        while n:
            ans=-ans-(n^(n-1))
            n&=n-1
        return abs(ans)

obj = Solution()
#data = obj.minimumOneBitOperations(n = 3)
data = obj.minimumOneBitOperations(n = 6)
print(data)