# Valid Parentheses
import io
class Solution:
    def isValidParentheses(self,s: str)->bool:
        t = 0
        for c in s:
            if c in ["{","(","["]:
                t += 1
            elif c in ["}",")","]"]:
                t -= 1    
        if t != 0:
            return False
        return True

obj = Solution()
data = obj.isValidParentheses(s="{[()]})")
print(data)