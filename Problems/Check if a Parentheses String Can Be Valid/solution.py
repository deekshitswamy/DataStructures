import io
from typing import List
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        b = a = 0
        for i in range(n):
            b += 1 if locked[i] == '0' or s[i] == '(' else -1
            if b < 0:
                return False
            a += 1 if locked[n - i - 1] == '0' or s[n - i - 1] == ')' else -1
            if a < 0:
                return False
        return True

obj = Solution()
#data = obj.canBeValid(s = "))()))", locked = "010100")
#data = obj.canBeValid(s = "()()", locked = "0000")
data = obj.canBeValid(s = ")", locked = "0")
print(data)