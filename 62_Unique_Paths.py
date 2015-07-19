class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        M=[[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            M[i][0]=1
        for i in range(n):
            M[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                M[i][j]=M[i-1][j]+M[i][j-1]
        return M[m-1][n-1]
