import io
import bisect
from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        beauty = []
        maxbeauty = items[0][1]
        beauty.append(maxbeauty)

        for i in range(1, len(items)):
            maxbeauty = max(items[i][1], maxbeauty)
            beauty.append(maxbeauty)

        result = []
        for query in queries:
            index = bisect.bisect_right(items, [query, float('inf')]) - 1
            if index >= 0:
                result.append(beauty[index])
            else:
                result.append(0)
        return result

obj = Solution()
#data = obj.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6])
#data = obj.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1])
data = obj.maximumBeauty(items = [[10,1000]], queries = [5])
print(data)