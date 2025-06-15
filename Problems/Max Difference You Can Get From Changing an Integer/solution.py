import io
from typing import List
class Solution:
    def maxDiff(self, num: int) -> int:
        sn = str(num)
        mx = sn[0]
        for i in sn:
            if i < '9':
                mx = i
                break
        mn = sn[0]
        n = len(sn)
        n2 = int(sn.replace(mx,'9'))
        sn = str(num)
        n1 = num
        if mn == '1':
            for i in range(1,n):
                if sn[i] > '1':
                    mn = sn[i]
                    n1 = int(sn.replace(mn,'0'))
                    break
        else:
            n1 = int(sn.replace(mn,'1'))

        return n2 - n1

obj = Solution()
#data = obj.maxDiff(num = 555)
data = obj.maxDiff(num = 9)
print(data)