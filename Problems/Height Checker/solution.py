import io
from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count

obj = Solution()
#data = obj.heightChecker(heights = [1,1,4,2,1,3])
#data = obj.heightChecker(heights = [5,1,2,3,4])
data = obj.heightChecker(heights = [1,2,3,4,5])
print(data)