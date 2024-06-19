import io
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def feasible(day: int) -> bool:
            bouquets = 0
            size = 0
            for bloom in bloomDay:
                if bloom <= day:
                    size += 1
                    if size == k:
                        bouquets += 1
                        size = 0
                else:
                    size = 0
            return bouquets >= m

        shortest, longest = min(bloomDay), max(bloomDay)
        while shortest < longest:
            day = shortest + (longest - shortest) // 2
            if feasible(day):
                longest = day
            else:
                shortest = day + 1
        return shortest

obj = Solution()
#data = obj.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1)
#data = obj.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2)
data = obj.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)
print(data)