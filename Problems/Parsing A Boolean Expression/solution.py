import io
from typing import List
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        pass

obj = Solution()
#data = obj.parseBoolExpr(expression = "&(|(f))")
#data = obj.parseBoolExpr(expression = "|(f,f,f,t)")
data = obj.parseBoolExpr(expression = "!(&(f,t))")
print(data)