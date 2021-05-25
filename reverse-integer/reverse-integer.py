class Solution:
    def reverse(self, x: int) -> int:
        
        MAX = (1 << 31) - 1
        MIN = (-1 << 31)
        r = 0
        is_negative = x < 0
        
        x = abs(x)
        
        while x: 
            x, m = divmod(x, 10)
            if (r > MAX / 10) or (r == MAX / 10 and m > 7):
                return 0
            if (r < MIN / 10) or (r == MIN / 10 and m < -8):
                return 0
            r = 10*r + m
        
        return -r if is_negative else r
      