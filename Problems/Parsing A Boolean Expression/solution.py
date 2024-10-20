import io
from typing import List
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for ch in expression:
            if ch == ',': continue
            if ch == ')':
                t = f = False
                while stk[-1] != '(':
                    top = stk.pop()
                    t |= top == 't'
                    f |= top == 'f'
                stk.pop()  
                op = stk.pop()  
                stk.append('t' if (op == '|' and t) or (op == '&' and not f) else 'f')
                if op == '!': stk[-1] = 'f' if t else 't'
            else: stk.append(ch)
        return stk[-1] == 't'

obj = Solution()
#data = obj.parseBoolExpr(expression = "&(|(f))")
#data = obj.parseBoolExpr(expression = "|(f,f,f,t)")
data = obj.parseBoolExpr(expression = "!(&(f,t))")
print(data)