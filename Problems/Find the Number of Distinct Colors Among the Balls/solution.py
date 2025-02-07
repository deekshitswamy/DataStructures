import io
from typing import List
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors={}
        balls={}
        cnt=0
        res=[]
        for query in queries:
            x,y = query[0],query[1]
            if x not in balls:
                if y not in colors or colors[y]<=0:
                    colors[y]=0
                    cnt+=1
                colors[y]+=1
            else:
                old_c=balls[x]
                colors[old_c]-=1
                if colors[old_c]==0:
                    cnt-=1
                    
                if y not in colors or colors[y]==0:
                    colors[y]=0
                    cnt+=1
                colors[y]+=1

            balls[x]=y
            res.append(cnt)
        return res

obj = Solution()
#data = obj.queryResults(limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]])
data = obj.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]])
print(data)