import io
import heapq
from typing import List

class SeatManager:

    def __init__(self, n: int):
        self.heap=list(range(1,n+1))

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
seatNumber = 3
n = 5
obj = SeatManager(n)
param_1 = obj.reserve()
obj.unreserve(seatNumber)



# obj = Solution()
# #data = obj.testfunc(n = 1)
# data = obj.testfunc(n = 2)
# data = obj.testfunc(n = 2)
# print(data)