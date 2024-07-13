import io
from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        #collect all robots
        robots = []
        for i in range(len(positions)):
            robots.append([i, positions[i], healths[i], directions[i]])
        
        #sort by posotions
        robots.sort(key=lambda robot: robot[1])

        ans = []

        stack = deque()
        for robot in robots:
            # riding left with no resistance => will survive
            if robot[3] == "L" and not stack:
                ans.append(robot)

            # riding right => add to stack
            elif robot[3] == "R":
                stack.append(robot)

            # riding left => let's find out how many collisions he will survive
            else:
                ridingLeft = robot
                while stack and ridingLeft[2] > 0 and ridingLeft[2] > stack[-1][2]:
                    stack.pop()
                    ridingLeft[2] -= 1
                
                # if Giga Chad (killed'em all and survived)
                if not stack and ridingLeft[2] > 0:
                    ans.append(ridingLeft)
                
                # if has been killed
                elif ridingLeft[2] < stack[-1][2]:
                    stack[-1][2] -= 1
                    if stack[-1][2] <= 0:
                        stack.pop()

                # if both dies
                elif ridingLeft[2] == stack[-1][2]:
                    stack.pop()

        # last survivors
        while stack:
            ans.append(stack.pop())

        # sort by input indexes
        ans.sort(key=lambda robot: robot[0])

        # return only health for each robot
        return [robot[2] for robot in ans]

obj = Solution()
#data = obj.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR")
#data = obj.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL")
data = obj.survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL")
print(data)