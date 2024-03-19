import io
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans=[0]*26
        for task in tasks:
            ans[ord(task)-ord('A')]+=1
        ans.sort()
        chunk=ans[25]-1
        idle=chunk*n
        for i in range(24,-1,-1):
            idle-=min(chunk,ans[i])
        if idle>=0:
            return len(tasks)+idle
        else:
            return len(tasks)

obj = Solution()
#data = obj.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
#data = obj.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1)
data = obj.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3)
print(data)