import io
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def valid(ip):
            if ip==ip[-1::-1]:
                return True
            return False
        
        def solve(ip,op):
            if ip=='':
                ans.append(op[:])
                return
            for i in range(1,len(ip)+1):
                if valid(ip[:i]):
                    op.append(ip[:i])
                    solve(ip[i:],op)
                    op.pop()
        ans=[]
        solve(s,[])
        return ans

obj = Solution()
#data = obj.partition(s = "aab")
data = obj.partition(s = "a")
print(data)