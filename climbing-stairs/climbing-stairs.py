class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: 
            return 1
        elif n == 2:
            return 2
        
        first, second, third = 1, 2, 3
        
        
        for i in range(3,n+1):
            third = first + second
            first, second = second, third
            
        return third
        
     