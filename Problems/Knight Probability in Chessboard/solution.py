import io
import collections
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directs = [[-2,1],[-1,2],[1,2],[2,1],
                   [-2,-1],[-1,-2],[1,-2],[2,-1]]
        pos = collections.deque([(1,[row, column])])
        while len(pos) and k:
            l = len(pos)
            node_len = l
            step_prob = {}
            while node_len:
                prob, (x,y) = pos.popleft()
                #print(x,y)
                for direct in directs:
                    dx, dy = direct
                    # vaild
                    #print(x+dx,y+dy)
                    if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<n:
                        #print(x+dx,y+dy)
                        if (x+dx,y+dy) not in step_prob:
                            step_prob[(x+dx,y+dy)] = 0
                        step_prob[(x+dx,y+dy)] += prob*1/8
                node_len-=1
            #print(step_prob)
            for key, prob in step_prob.items():
                pos.append((prob, key))
            k-=1

        return sum([x[0] for x in pos]) 

obj = Solution()
#data = obj.knightProbability(n = 3, k = 2, row = 0, column = 0)
data = obj.knightProbability(n = 1, k = 0, row = 0, column = 0)
print(data)