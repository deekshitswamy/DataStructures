import io
from typing import List
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans=0
        while left<right:
            left=left>>1
            right=right>>1
            ans+=1
        return left<<ans

obj = Solution()
#data = obj.rangeBitwiseAnd(left = 5, right = 7)
#data = obj.rangeBitwiseAnd(left = 0, right = 0)
data = obj.rangeBitwiseAnd(left = 1, right = 2147483647)
print(data)