class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # most pythonic solution, but some people might not consider this to be in place ...
        # matrix[:] = map(list, zip(*matrix[::-1]))

        
        # in place: just do transponation + reflection of matrix in place
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            for j in range(len(matrix) - len(matrix)//2):
                row[j], row[~j] = row[~j], row[j]
                    
                                           