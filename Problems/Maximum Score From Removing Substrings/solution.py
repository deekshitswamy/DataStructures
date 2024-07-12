import io
from typing import List
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y: #swap a, b
            s = s.replace('a', '_')
            s = s.replace('b', 'a')
            s = s.replace('_', 'b')
            x, y = y, x
        
        # x >= y
        ss = ''.join([x if x == 'a' or x == 'b' else '_' for x in s])
        ss = ss.split('_')
        print(ss)

        ans = 0
        for s in ss:
            totalChange = min(s.count('a'), s.count('b')) # z
            # print(s, totalChange)
            numAs = 0 
            numBs = 0

            cur = 0 # v
            for c in s:
                if c == 'a':
                    numAs += 1
                elif c == 'b':
                    if numAs > 0:
                        cur += 1 # counting the number of pairings
                        numAs -= 1
            
            ans += cur*x
            ans += (totalChange - cur)* y
        
        return ans

obj = Solution()
#data = obj.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5)
data = obj.maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4)
print(data)