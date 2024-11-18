import io
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        a = 1
        if k > 0:
            a*=1
            l = code[:k]
            s = code+l
        else:
            a*=-1
            l = code[k:]
            k*=-1
            s = l+code
        print(s)
        res = []
        cul = []
        for i in range(k):
            cul.append(s[i])
        res.append(sum(cul))
        if not cul:
            return [0]*len(code)
        for i in range(k,len(s)):
            cul.pop(0)
            cul.append(s[i])
            if len(cul)==k:
                res.append(sum(cul))
        if a==1:
            return res[1:]
        return res[:-1]

obj = Solution()
#data = obj.decrypt(code = [5,7,1,4], k = 3)
#data = obj.decrypt(code = [1,2,3,4], k = 0)
data = obj.decrypt(code = [2,4,9,3], k = -2)
print(data)