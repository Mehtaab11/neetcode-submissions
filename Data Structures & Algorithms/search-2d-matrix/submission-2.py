class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) 
        m = len(matrix[0]) 
        low = 0      
        high =( m * n) - 1

        while low <= high:
            mid = low + (high - low) // 2
               
            r = mid // m 
            c = mid % m 

            if matrix[r][c] < target:
                low = mid + 1 
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                return True

        return False





