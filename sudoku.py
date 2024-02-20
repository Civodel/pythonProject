from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid=True

        for miniboard in board:
            unique_entry = []
            for number in miniboard:
                if str(number) in unique_entry and str(number)!='.':
                    return False
                else:
                    unique_entry.append(str(number))
        unique_entry=[]

        acum=0
        for index in range(9):

            if acum==9:
                acum=0

            for sudoku_row in board:
                print(f"this{sudoku_row}")

                for i in range(3):

                    if acum<=i:
                        acum=i



                    if str(sudoku_row[i]) in unique_entry and str(sudoku_row[i]) != '.':
                        return False
                    else:
                        unique_entry.append(str(sudoku_row[i]))
                    print(unique_entry)

                    if len(unique_entry) == 9:
                        print(i)
                        print("hola")
                        acum=acum+1

                        unique_entry=[]
            unique_entry=[]

        for i in range(9):
            unique_entry=[]
            for sudoku_column in board:
                if str(sudoku_column[i]) in unique_entry and str(sudoku_column[i])!='.':
                    return False
                else:
                    unique_entry.append(str(sudoku_column[i]))

        return is_valid





sudoku = Solution()

'''
print(sudoku.isValidSudoku([[".",".",".",".","5",".",".","1","."],
                            [".","4",".","3",".",".",".",".","."],
                            [".",".",".",".",".","3",".",".","1"],
                            ["8",".",".",".",".",".",".","2","."],
                            [".",".","2",".","7",".",".",".","."],
                            [".","1","5",".",".",".",".",".","."],
                            [".",".",".",".",".","2",".",".","."],
                            [".","2",".","9",".",".",".",".","."],
                            [".",".","4",".",".",".",".",".","."]]))
'''
print(sudoku.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))