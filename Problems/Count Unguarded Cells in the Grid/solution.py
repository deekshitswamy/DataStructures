import io
from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        g=guards
        w=walls
        ip=[]
        for i in range(m):
            ip.append([0]*n)
        for i in g:
            ip[i[0]][i[1]]='G'
        for i in w:
            ip[i[0]][i[1]]='W'
        def blockcell(i,j):
            a,b=i,j
            #For RIGHT
            if j<n-1:
                a,b=i,j
                while(b<n-1):
                    if ip[a][b+1]!='W' and ip[a][b+1]!='G':
                        ip[a][b+1]=-1 
                        b+=1
                    else:
                        break
                
            #For LEFT 
            if j>0:
                a,b=i,j
                while(b>0):
                    if ip[a][b-1]!='W' and ip[a][b-1]!='G':
                        ip[a][b-1]=-1
                        b-=1 
                    else:
                        break
            #For UP 
            if i>0:
                a,b=i,j
                while(a>0):
                    if ip[a-1][b]!='W' and ip[a-1][b]!='G':
                        ip[a-1][b]=-1 
                        a-=1 
                    else:
                        break
                
            #For DOWN 
            if i<m-1:
                a,b=i,j
                while(a<m-1):
                    if ip[a+1][b]!='W' and ip[a+1][b]!='G':
                        ip[a+1][b]=-1 
                        a+=1 
                    else:
                        break
                
        for k in g:
            blockcell(k[0],k[1])
        op=0
        for i in ip:
            op+=i.count(0)
        return op

obj = Solution()
#data = obj.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])
data = obj.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])
print(data)