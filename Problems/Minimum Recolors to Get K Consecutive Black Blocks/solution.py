import io
from typing import List
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, white = 0, 0
        for i in range(len(blocks)):
            if i < k:
                if blocks[i] == 'W':
                    white += 1
                if i == k - 1:
                    res = white
            else:
                if blocks[i - k] == 'W':
                    white -= 1
                if blocks[i] == 'W':
                    white += 1

            res = min(res, white)

        return res

obj = Solution()
#data = obj.minimumRecolors(blocks = "WBBWWBBWBW", k = 7)
data = obj.minimumRecolors(blocks = "WBWBBBW", k = 2)
print(data)