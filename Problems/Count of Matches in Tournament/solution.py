import io
from typing import List
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans=0
        while n>1:
            ans+=(n//2)
            n=(n//2)+(n%2)
        return ans

obj = Solution()
#data = obj.numberOfMatches(n = 7)
data = obj.numberOfMatches(n = 14)
print(data)