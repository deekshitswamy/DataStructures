import io
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survived_asteroids=[]
        for asteroid in asteroids:
            while survived_asteroids and survived_asteroids[-1]>0 and asteroid<0:
                if survived_asteroids[-1]+asteroid<0:
                    survived_asteroids.pop()
                elif survived_asteroids[-1]+asteroid>0:
                    break
                else:
                    survived_asteroids.pop()
                    break
            else:
                survived_asteroids.append(asteroid)
        return survived_asteroids
            
obj = Solution()
data = obj.asteroidCollision(asteroids = [5,10,-5])
# data = obj.asteroidCollision(asteroids = [8,-8])
# data = obj.asteroidCollision(asteroids = [10,2,-5])
print(data)