import io
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj={}
        for ticket in tickets:
            adj[ticket[0]]=[]
            adj[ticket[1]]=[]

        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])

        for l in adj.values():
            l.sort()

        ans=[]
        def helper(node):
            while adj[node]:
                helper(adj[node].pop(0))

            ans.append(node)
        helper("JFK")
        return reversed(ans) 

obj = Solution()
#data = obj.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
data = obj.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print(data)