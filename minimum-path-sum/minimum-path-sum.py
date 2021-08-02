class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # prepare the left and top border
        for i in range(1,len(grid)):
            grid[i][0] += grid[i-1][0]
        for i in range(1,len(grid[0])):
            grid[0][i] += grid[0][i-1]
        
        # find min path sum
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]