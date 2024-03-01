import io
from typing import List
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = 0
        for i in s:
            if(i is '1'):
                one+=1

        length = len(s)
        remaining_len = length - one
        result = '1'*(one-1) + '0'*remaining_len + '1'
        return result

obj = Solution()
#data = obj.maximumOddBinaryNumber(s = "010")
data = obj.maximumOddBinaryNumber(s = "0101")
print(data)