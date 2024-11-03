import io
from typing import List
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        else:
            for i in range(len(s)):
                s = s[1:] + s[0]
                if s == goal:
                    return True
        return False

obj = Solution()
#data = obj.rotateString(s = "abcde", goal = "cdeab")
data = obj.rotateString(s = "abcde", goal = "abced")
print(data)