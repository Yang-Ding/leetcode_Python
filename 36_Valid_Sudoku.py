class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        characterset=['1','2','3','4','5','6','7','8','9','.']
        for i in range(9):
            L=[]
            for j in range(9):
                if board[i][j] not in characterset:
                    return False
                elif board[i][j]!='.':
                    L.append(board[i][j])
            if len(L)!=len(set(L)):
                return False
        for j in range(9):
            L=[]
            for i in range(9):
                if board[i][j]!='.':
                    L.append(board[i][j])
            if len(L)!=len(set(L)):
                return False
        offset=[(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for k in range(9):
            L=[]
            for i in range(3):
                for j in range(3):
                    if board[i+offset[k][0]][j+offset[k][1]]!='.':
                        L.append(board[i+offset[k][0]][j+offset[k][1]])
            if len(L)!=len(set(L)):
                return False
        return True
