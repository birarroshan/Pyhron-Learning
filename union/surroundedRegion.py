from typing import List
class Solution:
    #visited = set()

    def checkSafeZone(self,board: List[List[str]],i,j,l,w):
        print("---------------------------------")
        if  0<=i<l and 0<=j<w and  board[i][j] == "O" :
            print("Calling with i,j ",i,j,board[i][j])
            #self.visited.add((i,j))
            board[i][j] = "T"
            self.checkSafeZone(board,i+1,j,l,w)
            self.checkSafeZone(board,i,j+1,l,w)
            self.checkSafeZone(board,i-1,j,l,w)
            self.checkSafeZone(board,i,j-1,l,w)
            

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = len(board)
        w = len(board[0])

        if l <=1 or w<=1:
            return

        self.visited = set()

        # Top and bottom rows
        for j in range(w):
            if board[0][j] == "O":
                self.checkSafeZone(board, 0, j, l, w)
            if board[l-1][j] == "O":
                self.checkSafeZone(board, l-1, j, l, w)

        # Left and right columns
        for i in range(l):
            if board[i][0] == "O":
                self.checkSafeZone(board, i, 0, l, w)
            if board[i][w-1] == "O":
                self.checkSafeZone(board, i, w-1, l, w)
        print("Final Borad")
        print(board)

        for i in range(l):
            for j in range(w):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        print("Final Borad")
        print(board)
        
        # for i in board[0]:            
        #     if i == "O":
        #         i = "T"
        # for i in board[l-1]:            
        #     if i == "O":
        #         i = "T"
        # for i in range(0,w-1):            
        #     if board[0][i] == "O":
        #         board[0][i] = "T"
        #     if board[l-1][i] == "O":
        #         board[l-1][i] = "T"
        
        # i = 0
        # j = 0
        # while i<l and j<w:
        #     if board[i][j] == "O":
        #         if i == 0 or j==0 :
        #             board[i][j] = "T"
                

                


        # for i in range(1,l-1):
        #     for k in range(1,w-1):
        #         if board[i][k] == "O":
        #             if  (i==1 or k==1):
        #                 # print("Top or Left boundry- check left and top")
        #                 # print(board[i-1][k],board[i][k-1])
        #                 if "O" not in [board[i-1][k],board[i][k-1]]:
        #                     # print("Before:",i,k,board[i][k])
        #                     board[i][k] = "X"
        #                     # print("After ",board[i][k])
        #                     # print("\nBoard",board)
        #             elif  (i==l-2 or k==w-2):
        #                 # print("Bottom or Right boundry- ")
        #                 # print( board[i-1][k],board[i][k-1],board[i-1][k-1],board[i+1][k+1])
        #                 if "O" not in [board[i][k+1],board[i+1][k]]:
        #                     # print("Before:",i,k,board[i][k])
        #                     board[i][k] = "X"
        #                     # print("After ",board[i][k])
        #                     # print("\nBoard",board)
        #             else:
        #                 # print("Middle area")
        #                 # print(board[i-1][k],board[i][k-1],board[i-1][k-1],board[i+1][k+1])
        #                 if "O" not in [board[i-1][k],board[i][k-1],board[i-1][k-1],board[i+1][k+1]]:
        #                     # print("Before:",i,k,board[i][k])
        #                     board[i][k] = "X"
        #                     # print("After ",board[i][k])
        # print("\nBoard",board)

s = Solution()

mat  = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]
s.solve(mat)