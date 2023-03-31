# https://leetcode.com/problems/valid-sudoku/

import collections

# extreme verbose solution
class Solution:

    def isValidSudoku( board) :

        def containsDigits(list):
            digits=['1','2','3','4','5','6','7','8','9']
        
            for n in list:
                if(n not in digits):
                    return False
            return True


        def validBoard(board):
            isvalid=True
            for i in range(len(board)):
                list=[n for n in board[i] if n!="."]
               
                if(not containsDigits(list) or len(list)!=len(set(list))):
                    isvalid=False
                    break
                else:
                    continue
                
            return isvalid
        
        colBoard=[]

        for i in range(9):
            col=[]
            for j in range(9):
                col.append(board[j][i])
        
            colBoard.append(col)
        
        
        sub_board=[]

        for i in range(0,9,3):
            for j in range(0,9,3):
                list=[]
            
                list.extend(board[i][j:j+3])
                list.extend(board[i+1][j:j+3])
                list.extend(board[i+2][j:j+3])
                
                sub_board.append(list)
                
        return validBoard(board) and validBoard(sub_board) and validBoard(colBoard)
 

 # neetcode solution
def isValidSudoku2(board):

    cols=collections.defaultdict(set)
    rows=collections.defaultdict(set)
    squares=collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c]==".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3,c//3)]):
                
                return False
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])
            
    return True