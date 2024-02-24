import io
import itertools
from typing import List
from collections import defaultdict
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        groups=itertools.groupby(meetings,key=lambda x:x[2])
        ans={0,firstPerson}
        for key,grp in groups:
            res=set()
            graph=defaultdict(list)
            for a,b,t in grp:
                graph[a].append(b)
                graph[b].append(a)
                if a in ans:
                    res.add(a)
                if b in ans:
                    res.add(b)

            seen=list(res)[::]
            while seen:
                node=seen.pop()
                for i in graph[node]:
                    if i not in ans:
                        ans.add(i)
                        seen.append(i)
        return list(ans)

obj = Solution()
#data = obj.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1)
#data = obj.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3)
data = obj.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1)
print(data)