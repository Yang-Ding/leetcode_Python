class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        for i in xrange(1,m):
            grid[i][0]+=grid[i-1][0]
        for i in xrange(1,n):
            grid[0][i]+=grid[0][i-1]
        for i in xrange(1,m):
            for j in xrange(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
