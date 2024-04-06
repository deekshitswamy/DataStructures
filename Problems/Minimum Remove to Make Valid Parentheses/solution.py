import io
from typing import List
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans=[]
        n=len(s)
        S=list(s)
        for i in range(n):
            if S[i]=="(":
                ans.append(i)
            elif S[i]==")":
                if ans:
                    ans.pop()
                else:
                    S[i]=""
        for j in ans:
            S[j]=""
        return "".join(S)

obj = Solution()
#data = obj.minRemoveToMakeValid(s = "lee(t(c)o)de)")
#data = obj.minRemoveToMakeValid(s = "a)b(c)d")
data = obj.minRemoveToMakeValid(s = "))((")
print(data)