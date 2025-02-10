import io
from typing import List
class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isdigit():
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)

obj = Solution()
#data = obj.clearDigits(s = "abc")
data = obj.clearDigits(s = "cb34")
print(data)