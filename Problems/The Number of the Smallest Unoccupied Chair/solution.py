import io
from typing import List
from heapq import heappop, heappush
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        timeline = [] # stores (eventTime, isArrivingEvent, friendNumber)
        for i, (arrive, leaving) in enumerate(times):
            timeline.append((arrive, 1, i)) 
            timeline.append((leaving, 0, i)) # handle leaving events before arriving
        timeline.sort()

        heap = [i for i in range(n)] # stores the empty seat numbers as a heap, so we can always get smallest number
        rooms = [-1] * n # the seat number that each friend is occupying
        for _, isArrive, friend in timeline:
            if friend == targetFriend:
                return heap[0]
            if isArrive: # when friend arrive, assign it smallest chair
                room = heappop(heap)
                rooms[friend] = room
            else: # when friend leave, push the chair back to heap
                room = rooms[friend]
                heappush(heap, room)

obj = Solution()
#data = obj.smallestChair(times = [[1,4],[2,3],[4,6]], targetFriend = 1)
data = obj.smallestChair(times = [[3,10],[1,5],[2,6]], targetFriend = 0)
print(data)