import io
from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N:int = len(s)
        rotation = [0]*(N+1)
        res = []
        for i in range(len(shifts)):
            start, end, dir = shifts[i]
            dir = -1 if dir == 0 else 1
            rotation[start] += dir
            rotation[end+1] -= dir

        prefixSum = 0
        for i in range(N):
            prefixSum += rotation[i]
            newChar = chr((ord(s[i]) - ord('a') + prefixSum) % 26 + ord('a'))
            res.append(newChar)

        return ''.join(res)

obj = Solution()
#data = obj.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
data = obj.shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]])
print(data)