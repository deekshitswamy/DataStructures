import io
from typing import List
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

obj = Solution()
#data = obj.hammingWeight(n = 00000000000000000000000000001011)
#data = obj.hammingWeight(n = 00000000000000000000000010000000)
data = obj.hammingWeight(n = 11111111111111111111111111111101)
print(data)