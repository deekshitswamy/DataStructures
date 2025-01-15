import io
from typing import List
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bit_1 = num1.bit_count()
        set_bit_2 = num2.bit_count()

        if set_bit_1 > set_bit_2:
            diff = set_bit_1 - set_bit_2
            i = 0
            while diff > 0:
                if num1 & (1 << i) :
                    num1 -= (1 << i)
                    diff -= 1
                i += 1
        else:
            diff = set_bit_2 - set_bit_1
            i = 0
            while diff > 0:
                if not (num1 & (1 << i)) :
                    num1 += (1 << i)
                    diff -= 1
                i += 1

        return num1

obj = Solution()
#data = obj.minimizeXor(num1 = 3, num2 = 5)
data = obj.minimizeXor(num1 = 1, num2 = 12)
print(data)