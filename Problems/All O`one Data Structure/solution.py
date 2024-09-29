import io
from typing import List
class AllOne:

    def __init__(self):
        self.d = defaultdict(int)
        self.high = []
        self.low = []

    def inc(self, key: str) -> None:
        self.d[key]+=1
        heapq.heappush(self.low,(self.d[key],key))
        heapq.heappush(self.high,(-self.d[key],key))

    def dec(self, key: str) -> None:
        self.d[key]-=1
        if self.d[key]:
            heapq.heappush(self.low,(self.d[key],key))
            heapq.heappush(self.high,(-self.d[key],key))

    def getMaxKey(self) -> str:
        while self.high:
            a,k = heapq.heappop(self.high)
            if self.d[k] == -a:
                heapq.heappush(self.high,(a,k))
                return k
        return ""

    def getMinKey(self) -> str:
        while self.low:
            a,k = heapq.heappop(self.low)
            if self.d[k] == a:
                heapq.heappush(self.low,(a,k))
                return k
        return ""
        


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.dec("hello")
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()