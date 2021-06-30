class Solution:
    
    def mySqrt(self, x: int) -> int:
        guess = x / 2
        
        while abs(guess*guess - x) > 0.1:
            guess = (guess + x/guess) / 2
        
        print(guess)
        return int(guess)