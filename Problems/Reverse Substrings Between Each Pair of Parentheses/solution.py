import io
from typing import List
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(char)
        return ''.join(stack)

obj = Solution()
#data = obj.reverseParentheses(s = "(abcd)")
#data = obj.reverseParentheses(s = "(u(love)i)")
data = obj.reverseParentheses(s = "(ed(et(oc))el)")
print(data)