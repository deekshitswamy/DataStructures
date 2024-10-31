import io
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        memo = {}

        def helper(currRobot, currFact, usedCapacity):
            if currRobot == len(robot):
                return 0
            if currFact == len(factory):
                return float('inf')
            key = (currRobot, currFact, usedCapacity)
            if key in memo:
                return memo[key]

            minDist = helper(currRobot, currFact+1, 0)
            position, capacity = factory[currFact]
            if usedCapacity < capacity:
                dist = abs(robot[currRobot] - position)
                minDist = min(minDist, dist + helper(currRobot+1, currFact, usedCapacity + 1))
            memo[key] = minDist
            return minDist
        return helper(0,0,0)

obj = Solution()
#data = obj.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]])
data = obj.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]])
print(data)