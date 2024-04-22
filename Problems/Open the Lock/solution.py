import io
from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        q=deque([("0000",0)])
        visited=set()
        while q:
            cand,steps=q.popleft()
            if cand==target:
                return steps
            for i in range(4):
                for digit in [((int(cand[i])+1)%10),((int(cand[i])-1)%10)]:
                    nx=cand[:i]+str(digit)+cand[1+i:]
                    if nx not in deadends and nx not in visited:
                        visited.add(nx)
                        q.append((nx,steps+1))
        return -1

obj = Solution()
#data = obj.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
#data = obj.openLock(deadends = ["8888"], target = "0009")
data = obj.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888")
print(data)