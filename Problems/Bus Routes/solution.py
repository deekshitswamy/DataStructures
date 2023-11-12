import io
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        graph=defaultdict(set)
        for routes_id,stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(routes_id)
                
        queue=deque([(source,0)])
        seen_stops=set([source])
        seen_routes=set()
        while queue:
            stop,new_changes=queue.popleft()
            
            if stop==target:
                return new_changes
            
            for routes_id in graph[stop]:
                if routes_id not in seen_routes:
                    seen_routes.add(routes_id)
                    
                    for stop in routes[routes_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop,new_changes+1))
                            
        return -1

obj = Solution()
#data = obj.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
data = obj.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12)
print(data)