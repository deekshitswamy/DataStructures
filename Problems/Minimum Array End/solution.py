import io
from typing import List
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        X = bin(x)[2:].zfill(64)
        N = bin(n - 1)[2:].zfill(64)
        result = ['0'] * 64
        j = 0

        for i in range(64):
            if X[-1 - i] == '1':
                result[-1 - i] = '1'
            else:
                result[-1 - i] = N[-1 - j]
                j += 1

        return int(''.join(result), 2)

obj = Solution()
#data = obj.minEnd(n = 3, x = 4)
data = obj.minEnd(n = 2, x = 7)
print(data)