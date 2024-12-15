import io
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        n = len(classes)

        for p, t in classes:
            heapq.heappush(max_heap, (p / t - (p + 1) / (t + 1), p, t))

        while extraStudents > 0:
            _, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1

            heapq.heappush(max_heap, (p / t - (p + 1) / (t + 1), p, t))
            extraStudents -= 1

        result = sum([p / t for _, p, t in max_heap])

        return result / n

obj = Solution()
#data = obj.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
data = obj.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4)
print(data)