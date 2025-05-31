import io
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        queue = deque([(1, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[n - 1][0] = True
        
        while queue:
            value, dist = queue.popleft()
            
            if value == n * n:
                return dist
            
            for next_val in range(value + 1, min(value + 6, n * n) + 1):
                i = n - 1 - (next_val - 1) // n
                j = (next_val - 1) % n if (n - 1 - i) % 2 == 0 else n - 1 - (next_val - 1) % n
                
                if board[i][j] != -1:
                    next2 = board[i][j]
                    i2 = n - 1 - (next2 - 1) // n
                    j2 = (next2 - 1) % n if (n - 1 - i2) % 2 == 0 else n - 1 - (next2 - 1) % n
                    if not visited[i2][j2]:
                        visited[i2][j2] = True
                        queue.append((next2, dist + 1))
                else:
                    if not visited[i][j]:
                        visited[i][j] = True
                        queue.append((next_val, dist + 1))
        
        return -1

obj = Solution()
#data = obj.snakesAndLadders(board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
data = obj.snakesAndLadders(board = [[-1,-1],[-1,3]])
print(data)