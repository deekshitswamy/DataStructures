import io
from typing import List
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        for i in matches:
            w, l = i[0], i[1]
            if w not in losses: losses[w] = 0
            if l not in losses: losses[l] = 1
            else: losses[l] += 1
        answer = [sorted([i for i in losses if losses[i] == 0]), sorted([i for i in losses if losses[i] == 1])]
        return answer

obj = Solution()
#data = obj.findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
data = obj.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]])
print(data)