class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if len(matrix)==0:
            return 0
        maxl=0
        m=len(matrix)
        n=len(matrix[0])
        M=[[0 for col in range(n)]for row in range(m)]
        if matrix[0][0]=="1":
            maxl=1
            M[0][0]=1
        for i in range(1,m):
            if matrix[i][0]=="1":
                M[i][0]=1
        for i in range(1,n):
            if matrix[0][i]=="1":
                M[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=="1":
                    M[i][j]=min(M[i][j-1],M[i-1][j-1],M[i-1][j])+1
        for i in range(m):
            for j in range(n):
                if M[i][j]>maxl:
                    maxl=M[i][j]
        return maxl*maxl
