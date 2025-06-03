import io
from typing import List
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n, ans = len(status), 0
        queue, seen, owned, has_key = deque(), set(), set(initialBoxes), set()
        
        for box in initialBoxes:
            if status[box]: queue.append(box)
        
        while queue:
            box = queue.popleft()
            if box in seen: continue
            seen.add(box)
            ans += candies[box]
            for k in keys[box]:
                if k not in has_key:
                    has_key.add(k)
                    if k in owned and k not in seen:
                        queue.append(k)
            for b in containedBoxes[box]:
                owned.add(b)
                if status[b] or b in has_key:
                    queue.append(b)
        
        return ans

obj = Solution()
#data = obj.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])
data = obj.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])
print(data)