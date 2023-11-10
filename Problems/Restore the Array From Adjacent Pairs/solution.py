import io
from typing import List
import collections

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjs=collections.defaultdict(set)
        for i,j in adjacentPairs:
            adjs[i].add(j)
            adjs[j].add(i)

        for node,adj in adjs.items():
            if len(adj)==1:
                break
        ans=[node]
        while adjs[node]:
            new=adjs[node].pop()
            ans.append(new)
            adjs[new].remove(node)
            node=new
        return ans

obj = Solution()
#data = obj.restoreArray(adjacentPairs = [[2,1],[3,4],[3,2]])
#data = obj.restoreArray(adjacentPairs = [[4,-2],[1,4],[-3,1]])
data = obj.restoreArray(adjacentPairs = [[100000,-100000]])
print(data)