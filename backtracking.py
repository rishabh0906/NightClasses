


def KnightTour_Uti(Solution,Moves,sr,sc,move):
    Solution[sr][sc]=move
    if move==((len(Solution)*len(Solution))-1):
        return True


    res=False
    for i in range(len(Moves)):
        r=sr+Moves[i][0]
        c=sc+Moves[i][1]
        if r>=0 and r<len(Solution) and c>=0 and c<len(Solution[0]) and Solution[r][c]==-1:
            res=KnightTour_Uti(Solution,Moves,r,c,move+1)
            if res==True:
                return res                
           
    Solution[sr][sc]=-1    
    return res

def KnightTour(n):
    Solution =[[-1 for x in range(n)] for y in range(n)]
    print(Solution)

    Moves =[(-1,2),(1,-2),(1,2),(-1,-2),(-2,1),(2,1),(2,-1),(-2,-1)]



    KnightTour_Uti(Solution,Moves,0,0,0)
    print(Solution)


#KnightTour(8)

def MazePath_Shortest(sr,sc,n,m,Visited,Moves)->int:
    
    if sr==n-1 and sc==m-1:
        return 0

    Visited[sr][sc]=True

    ans= 10**9
    for i in range(len(Moves)):
        r=sr+Moves[i][0]
        c=sc+Moves[i][1]
        if r>=0 and r<n and c>=0 and c<m and Visited[r][c]==False:
           res=MazePath_Shortest(r,c,n,m,Visited,Moves)
           if ans>res+1:
               ans=res+1

    Visited[sr][sc]=False   
    return ans

def MazePath(n,m):

    Moves=[(-1,0),(1,0),(0,-1),(0,1)]

    Visited=[[False for i in range(n)] for j in range(m)]

    length= MazePath_Shortest(0,0,n,m,Visited,Moves)
    print(length)

MazePath(3,3)