class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        guess = num / 2
        
        while abs(guess*guess - num) > 0.1:
            guess = (guess + num/guess) / 2
        
        if (int(guess)*int(guess) == num):
            return True
    
        return False