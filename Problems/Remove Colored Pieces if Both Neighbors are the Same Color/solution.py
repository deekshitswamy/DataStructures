import io
import collections
from itertools import groupby
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c=collections.Counter()
        for x,t in groupby(colors):
            c[x]+=max(len(list(t))-2,0)
        if c['A']>c['B']:
            return True
        return False

obj = Solution()
#data = obj.winnerOfGame(colors = "AAABABB")
#data = obj.winnerOfGame(colors = "AA")
data = obj.winnerOfGame(colors = "ABBBBBBBAAA")
print(data)