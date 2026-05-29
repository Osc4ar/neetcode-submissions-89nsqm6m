class Solution:
    '''
    We can use sets to store the non-empty values of the Sudoku by row, column and sub-boxes.

    We would have a list of 9 sets for rows, a list of 9 sets for columns and a bidimensional list of 3x3 for the sub-boxes.

    While iterating the board, we check if the value we want to add exists in the target set, if it does we return False.
    If we finish iterating the whole board, we return True since it's valid.

    To map the current cell to the target sub-box we divide the indexes by 3 (integer division).

    The time complexity is: O(n^2) since we would be iterating all board cells once. n is the board size.
    The memory complexity is also O(n^2), specifically is O(3*n^2) because we are storing each element of the board thrice.
    But that can be simplified as O(n^2)
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [[set() for _ in range(3)] for _ in range(3)] # 3x3 board

        for i in range(len(board)):
            for j in range(len(board[i])):
                n = board[i][j]
                if n == '.':
                    continue 

                if n in rows[i]:
                    return False
                if n in cols[j]:
                    return False
                if n in sub_boxes[i // 3][j // 3]:
                    return False

                rows[i].add(n)
                cols[j].add(n)
                sub_boxes[i // 3][j // 3].add(n)
        
        return True