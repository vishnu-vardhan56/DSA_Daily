class Solution:
    def revers(matrix,n,m):
        l = 0
        r = len(matrix[0]) -1
        for i in range(n):
            l = 0
            r = len(matrix[i])-1
            while(l<r):
                matrix[i][l],matrix[i][r] = matrix[i][r],matrix[i][l] 
                l += 1
                r -= 1
            
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i,m):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp              
        Solution.revers(matrix,n,m)
        """
        Do not return anything, modify matrix in-place instead.
        """
        