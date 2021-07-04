class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        
        def is_on_border(x: int, y: int) -> bool:
            if x == len(grid)-1 or y == len(grid[x])-1 or x == 0 or y == 0:
                return True
            return False
        
        def is_in_bounds(x: int, y: int) -> bool:
            if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]):
                return True
            return False
    
        def dfs(x,y):
            directions = [
                (1,0),
                (0,1),
                (-1,0),
                (0,-1)
            ]
            
            for d in directions:
                dx, dy = x+d[0], y+d[1]
                if not is_in_bounds(dx,dy):
                    continue
                if grid[dx][dy] == 0:
                    grid[dx][dy] = 1
                    dfs(dx,dy)

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if is_on_border(x,y) and grid[x][y] == 0:
                    grid[x][y] = 1
                    dfs(x,y)
                                        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    ans +=1
                    dfs(x,y)
        
        return ans
        