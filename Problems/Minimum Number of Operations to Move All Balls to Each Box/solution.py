import io
from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left, right = 0, 0
        totalLeft, totalRight = 0, 0
        res = []
        for i in range(0, len(boxes)):
            if boxes[i] == '1':
                totalRight += i
                right += 1

        for i in range(0, len(boxes)):
            res.append(totalRight + totalLeft)
            if boxes[i] == '1':
                right -= 1
                left += 1
            totalLeft += left
            totalRight-=right
        return res

obj = Solution()
#data = obj.minOperations(boxes = "110")
data = obj.minOperations(boxes = "001011")
print(data)