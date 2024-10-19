import io
from typing import List
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        mid = (1 << (n - 1)) - 1  

        if k <= mid:
            return self.findKthBit(n - 1, k)
        elif k == mid + 1:
            return '1'
        else:
            return '1' if self.findKthBit(n - 1, (1 << n) - k) == '0' else '0'

obj = Solution()
#data = obj.findKthBit(n = 3, k = 1)
data = obj.findKthBit(n = 4, k = 11)
print(data)