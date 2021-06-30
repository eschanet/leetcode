class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        guess = num / 2
        
        while abs(guess*guess - num) > 0.1:
            guess = (guess + num/guess) / 2
        
        if (int(guess)*int(guess) == num) or (int(guess+1)*int(guess+1) == num):
            return True
    
        return False