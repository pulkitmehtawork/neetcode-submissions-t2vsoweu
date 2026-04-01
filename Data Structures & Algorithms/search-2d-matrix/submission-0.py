class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m  = len(matrix)
        n = len(matrix[0])

        # binary search for correspondng row
        l = 0
        
        r = m-1

        # logm -- for 
        row_num =-1
        while l <= r:
            mid = (l +r)//2
            val_start = matrix[mid][0]
            val_end = matrix[mid][-1]
            if val_start <= target <= val_end:
                row_num = mid
                break
            elif val_start < target:
                l += 1
            elif val_start > target:
                r -=1
        print(row_num)
        if row_num == -1:
            return False
        
        l =0
        r = n -1
        
        while l <=r:
            mid = (l + r) // 2
            if matrix[row_num][mid] ==  target:
                return True
            elif matrix[row_num][mid] < target:
                l += 1
            elif matrix[row_num][mid] > target:
                r -=1
        return False