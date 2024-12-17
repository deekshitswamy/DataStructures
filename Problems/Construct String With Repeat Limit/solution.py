import io
from typing import List
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freqmap = {}
        rlmap = {}

        for char in s:
            if char in freqmap:
                freqmap[char] += 1
            else:
                freqmap[char] = 1
            
            if char not in rlmap:
                rlmap[char] = repeatLimit
        
        order = sorted(list(freqmap.keys()), reverse=True)

        minPos = 0
        backup = minPos + 1
        res = []

        while minPos < len(order):
            bestchar = order[minPos]
            if rlmap[bestchar] > 0:
                res.append(bestchar)
                rlmap[bestchar] -= 1
                if backup < len(order):
                    backupchar = order[backup]
                    rlmap[backupchar] = repeatLimit
                freqmap[bestchar] -= 1
                if freqmap[bestchar] == 0:
                    minPos = backup 
                    backup += 1
            else:
                if backup < len(order):
                    backupchar = order[backup]
                    res.append(backupchar)
                    rlmap[bestchar] = repeatLimit
                    rlmap[backupchar] -= 1
                    freqmap[backupchar] -= 1
                    if freqmap[backupchar] == 0:
                        backup += 1  
                else:
                    minPos = backup  
        
        return "".join(res)

obj = Solution()
#data = obj.repeatLimitedString(s = "cczazcc", repeatLimit = 3)
data = obj.repeatLimitedString(s = "aababab", repeatLimit = 2)
print(data)