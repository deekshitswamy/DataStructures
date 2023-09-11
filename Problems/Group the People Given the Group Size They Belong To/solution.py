import io
import collections
from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans=[]
        group_map=collections.defaultdict(list)
        for i,group_size in enumerate(groupSizes):
            group_map[group_size].append(i)

        return [ids[i:i+k]
        for k,ids in group_map.items()
        for i in range(0,len(ids),k)]

obj = Solution()
data = obj.groupThePeople(groupSizes = [3,3,3,3,3,1,3])
#data = obj.groupThePeople(groupSizes = [2,1,3,3,3,2])
print(data)