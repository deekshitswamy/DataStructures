import io
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass

obj = Solution()
data = obj.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
#data = obj.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print(data)