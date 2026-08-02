class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row = 1:9
        column = 1:9

        grid = 3x3 --> 1:9

        """
        """
        row = set()
        col = set()
        
              0           1           2
          0   1   2   3   4   5   6   7   8
        ["1","2",".",".","3",".",".",".","."], 0
        ["4",".",".","5",".",".",".",".","."], 1  0
        [".","9","8",".",".",".",".",".","3"], 2
        ["5",".",".",".","6",".",".",".","4"], 3
        [".",".",".","8",".","3",".",".","5"], 4  1
        ["7",".",".",".","2",".",".",".","6"], 5
        [".",".",".",".",".",".","2",".","."], 6
        [".",".",".","4","1","9",".",".","8"], 7  2
        [".",".",".",".","8",".",".","7","9"]  8

        board[i][s]--> 
        [[1,2,3...]]
        index 3
        [start, stop, index]
        """
        row = {}
        col = {}
        res = {}

        # row = {
        #     0: set(1,2,3),
        #     1:
        # }

        for i in range(9):
            for s in range(9):
                if board[i][s] =='.':
                    continue

                if i not in row:
                    row[i] = set()
                if s not in col:
                    col[s] = set()
                if (i//3, s//3) not in res:
                    res[(i // 3, s // 3)] = set()

                if board[i][s] in row[i] or board[i][s] in col[s] or board[i][s] in res[(i//3,s//3)]:
                    return False
                    
                row[i].add(board[i][s])
                col[s].add(board[i][s])
                res[(i // 3, s // 3)].add(board[i][s])
                print(row, col, res)
        return True