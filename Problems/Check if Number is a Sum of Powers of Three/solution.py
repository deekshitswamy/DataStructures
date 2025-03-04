import io
from typing import List
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = math.floor(math.log(n, 3))

        while n >= 0 and power >= 0:
            value_of_max_pow = 3 ** power

            if n - value_of_max_pow < 0:
                power -= 1
                continue

            n -= value_of_max_pow
            power -= 1
            
            if n == 0:
                return True

        return False

obj = Solution()
#data = obj.checkPowersOfThree(n = 12)
#data = obj.checkPowersOfThree(n = 91)
data = obj.checkPowersOfThree(n = 21)
print(data)