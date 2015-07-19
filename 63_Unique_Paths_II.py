class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid): 
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        M=[[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]!=1:
                M[i][0]=1
            else:
                for j in range(i,m):
                    M[j][0]=0
                break
        for i in range(n):
            if obstacleGrid[0][i]!=1:
                M[0][i]=1
            else:
                for j in range(i,n):
                    M[0][j]=0
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    M[i][j]=0
                elif obstacleGrid[i][j-1]!=1 and obstacleGrid[i-1][j]!=1:
                    M[i][j]=M[i][j-1]+M[i-1][j]
                elif obstacleGrid[i][j-1]==1 and obstacleGrid[i-1][j]!=1:
                    M[i][j]=M[i-1][j]
                elif obstacleGrid[i][j-1]!=1 and obstacleGrid[i-1][j]==1: 
                    M[i][j]=M[i][j-1]
                else:
                    M[i][j]=0
        return M[m-1][n-1]
