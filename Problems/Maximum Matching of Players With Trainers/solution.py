import io
from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        res = 0
        i, j = 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
            j += 1
        return res

obj = Solution()
#data = obj.matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8])
data = obj.matchPlayersAndTrainers(players = [1,1,1], trainers = [10])
print(data)