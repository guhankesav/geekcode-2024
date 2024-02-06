class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        subboxes = collections.defaultdict(set)

        rowLength = len(board)
        columnLength = len(board[0])

        for i in range(rowLength):
            for j in range(columnLength):

                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in subboxes[(i//3,j//3)]:
                    return False

                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                subboxes[(i//3, j//3)].add(board[i][j])
                
        return True
        