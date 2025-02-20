import io
from typing import List
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        s='abc'
        def backtrack(comb):
            if len(comb)==n:
                res.append(comb)
                return
            for ch in s:
                if comb and comb[-1]==ch:
                    continue
                backtrack(comb+ch)
        backtrack("")

        return "" if k>len(res) else res[k-1]

obj = Solution()
#data = obj.getHappyString(n = 1, k = 3)
#data = obj.getHappyString(n = 1, k = 4)
data = obj.getHappyString(n = 3, k = 9)
print(data)
