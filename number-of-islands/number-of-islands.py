class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            
        def is_in_bounds(x: int,y: int) -> bool:
            if -1 < x < len(grid) and -1 < y < len(grid[x]):
                return True
            return False
        
        def dfs(x,y):
            directions = [
                (1,0),
                (0,1),
                (-1,0),
                (0,-1),
            ]

            for d in directions:
                dx, dy = x+d[0], y+d[1]
                if not is_in_bounds(dx,dy):
                    continue
                if int(grid[dx][dy]) == 1: 
                    grid[dx][dy] = 0
                    dfs(dx,dy)
        
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if int(grid[x][y]) == 1:
                    grid[x][y] = 0
                    ans += 1
                    dfs(x,y)
                    
        return ans
