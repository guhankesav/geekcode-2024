class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLength = len(matrix)
        columnLength = len(matrix[0])
        
        top, bottom = 0, rowLength - 1
        while top <= bottom:
            row = top + ((bottom - top) // 2)
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row -1
            else:
                break
        print(row)
        if not (top <= bottom):
            return False
        
        l, r = 0, columnLength - 1
        while l <= r:
            mid = l + ((r - l)//2)
            print(mid)
            if target < matrix[row][mid] :
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        print(mid)
        return False
        